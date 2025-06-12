import pandas as pd
import numpy as np

def trading_turn(df):
    df = df[['investSessionId', 
          'userId',
          'turn',
          'riskLevel',
          'transactionType']]
    
    df = df.groupby(['investSessionId', 'userId', 'turn'])['transactionType'].apply(lambda x: int((x != "KEEP").any())).reset_index(name="notAllKeep")
    df = df.groupby(['investSessionId', 'userId'])['notAllKeep'].mean().reset_index(name="avgNotKeep")
    
    return df

def transaction_num(df):
    df = df[['investSessionId', 
          'turn',
          'riskLevel',
          'plusClick',
          'minusClick']]

    df['click'] = df['plusClick'] + df['minusClick']
    df = df.groupby('investSessionId')[['click']].mean().reset_index()

    return df

def avg_cash_ratio(df, seed_df):
    df = df[['investSessionId', 
          'chapterId',
          'turn',
          'currentPoint']]

    df = df.groupby(['investSessionId', 'chapterId', 'turn'])['currentPoint'].mean().reset_index(name='avgCurrentValue')
    df = df.merge(seed_df, on='chapterId', how='left')
    df['diff'] = df['seedMoney'] - df['avgCurrentValue']
    df = df.groupby('investSessionId')['diff'].mean().reset_index(name="avgDiff")
    
    return df

def avg_stay_time(df):
    df = df[['investSessionId', 
                'turn',
                'startedAt',
                'endedAt']]
    
    df = df.drop_duplicates(subset=['investSessionId', 'turn']).copy()
    df['stayTime'] = (df['endedAt'] - df['startedAt']).dt.total_seconds()
    df.drop(columns=['startedAt', 'endedAt'], inplace=True)
    df = df.groupby('investSessionId')['stayTime'].mean().reset_index(name='avgStayTime')

    return df

def avg_trade_ratio(df):
    # 구매 데이터 생성
    transcation_df = df[['investSessionId',
                        'turn',
                        'riskLevel',
                        'numberOfShares',
                        'deltaShares']].copy()
    
    # 변화량에 따라 BUY/SELL 구분하기
    transcation_df['is_buy'] = np.where(
        transcation_df['deltaShares'] > 0, 
        transcation_df['deltaShares'], 
        0
    )

    transcation_df['is_sell'] = np.where(
        transcation_df['deltaShares'] < 0, 
        -transcation_df['deltaShares'],
        0
    )

    # 각 investSessionId, riskLevel 별로 buy/sell 개수 집계
    buy_sell_counts = transcation_df.groupby(['investSessionId', 'riskLevel'])[['is_buy', 'is_sell']].sum().reset_index()
    buy_sell_counts.rename(columns={'is_buy': 'buyCount', 'is_sell': 'sellCount'}, inplace=True)
    buy_sell_counts.head()

    # investSessionId별 전체 buy_count, sell_count 구하기
    total_buy = buy_sell_counts.groupby('investSessionId')['buyCount'].sum().reset_index(name='totalBuyCount')
    total_sell = buy_sell_counts.groupby('investSessionId')['sellCount'].sum().reset_index(name='totalSellCount')

    # 원본과 병합
    buy_sell_counts = buy_sell_counts.merge(total_buy, on='investSessionId')
    buy_sell_counts = buy_sell_counts.merge(total_sell, on='investSessionId')

    buy_sell_counts['buyRatio'] = buy_sell_counts['buyCount'] / buy_sell_counts['totalBuyCount']
    buy_sell_counts['sellRatio'] = buy_sell_counts['sellCount'] / buy_sell_counts['totalSellCount']

    buy_sell_counts.head()

# buy_ratio_pivot: 열로 riskLevel을 펼치기  
    buy_ratio_pivot = buy_sell_counts.pivot(index='investSessionId', columns='riskLevel', values='buyRatio')
    buy_ratio_pivot.columns = [f"{level}BuyRatio" for level in buy_ratio_pivot.columns]
    buy_ratio_pivot.reset_index(inplace=True)

# sell_ratio pivot: 열로 riskLevel을 펼치기
    sell_ratio_pivot = buy_sell_counts.pivot(index='investSessionId', columns='riskLevel', values='sellRatio')
    sell_ratio_pivot.columns = [f"{level}SellRatio" for level in sell_ratio_pivot.columns]
    sell_ratio_pivot.reset_index(inplace=True)

# merge 두 pivot
    avgTradeRatio = pd.merge(buy_ratio_pivot, sell_ratio_pivot, on='investSessionId')

    return avgTradeRatio

def tag_avg_stay_time(df):
    df = df[['investSessionId',
            'turn',
            'newsTag',
            'startedAt',
            'endedAt']].drop_duplicates()

    df = df[df['newsTag'] != "all"]
    df["turnDuration"] = df["endedAt"] = df["startedAt"]

    tagAvgStayTime = df.groupby("investSessionId")["turnDuration"].mean().reset_index().rename(columns={"turnDuration":"tagTrunDuraion"})
    tagAvgStayTime

    return tagAvgStayTime