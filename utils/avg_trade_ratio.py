import numpy as np
import pandas as pd

# 각 위험 별 구매/판매 비율
def avg_trade_ratio(df):
    # 구매 데이터 생성
    transcation_df = df[['investSessionId',
                        'turn',
                        'riskLevel',
                        'numberOfShares',
                        'deltaShares']]
    
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