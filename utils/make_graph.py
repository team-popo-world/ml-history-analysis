import pandas as pd
from db.merge_df import load_df
from utils.avg_stay_time import avg_stay_time
from utils.tag_avg_stay_time import tag_avg_stay_time
from utils.filtered_mean import filtered_mean
from utils.bet_buy_ratio import bet_buy_ratio
from utils.bet_sell_ratio import bet_sell_ratio
from utils.avg_cash_ratio import avg_cash_ratio
from utils.avg_trade_ratio import avg_trade_ratio

def make_df_graph1(userId):
    # 평균 턴 체류시간, tag 발생 턴 평균 체류시간 + 우리아이 나이대 평균 값
    df = load_df()

    df1 =avg_stay_time(df)
    df1 = filtered_mean(df1, "avgStayTime", userId)

    df2 = tag_avg_stay_time(df)
    df2 = filtered_mean(df2, "tagAvgStayTime", userId)

    fin_df = pd.merge(df1, df2, on="investSessionId", how="outer")

    return fin_df

def make_df_graph2_1(userId):
    # 종목별 구매 비율 영역 그래프
    df = load_df()

    df = avg_trade_ratio(df)
    df = df.loc[df["userId"] == userId, ["userId","investSessionId","highBuyRatio","midBuyRatio","lowBuyRatio"]]

    return df

def make_df_graph2_2(userId):
    # 종목별 판매 비율 영역 그래프
    df = load_df()

    df = avg_trade_ratio(df)
    df = df.loc[df["userId"] == userId, ["userId","investSessionId","highSellRatio","midSellRatio","lowSellRatio"]]
    
    return df

def make_df_graph2_3(userId):
    # 종목별 판매/구매 비율 누적 막대 그래프 vs 우리아이 나이대 평균균
    df = load_df()

    df = avg_trade_ratio(df)

    # 우리 아이랑 같은 나이를 갖는 행만 필터링
    child_age = df.loc[df["childId"]==userId, "age"].iloc[0] 
    df = df[df["age"] == child_age].copy()

    # Sell, Buy 각각 구분
    sell = df["userId","age","investSessionId","highSellRatio","midSellRatio","lowSellRatio"]
    buy = df["userId","age","investSessionId","highBuyRatio","midBuyRatio","lowBuyRatio"]

    sell.rename(columns={"highSellRatio" : "highRatio",
                         "midSellRatio" : "midRatio",
                         "lowSellRatio" : "lowRatio"},
                         inplace=True)
    
    buy.rename(columns={"highBuyRatio" : "highRatio",
                         "midBuyRatio" : "midRatio",
                         "lowBuyRatio" : "lowRatio"},
                         inplace=True)
    
    # sell/buy 구분 컬럼 (Type) 추가
    sell["Type"] = "Sell"
    buy["Type"] = "Buy"
    
    cols = ["highRatio", "midRatio", "lowRatio"]
    
    # 1. SELL
    # 우리아이 나이대 평균
    for col in cols:
        col_mean = sell[f"{col}"].mean()
        sell[f'Avg{col}Age'] = col_mean
    
    # 우리아이 평균
    filtered_sell = sell[sell["userId"] == userId]

    for col in cols:
        my_mean = filtered_sell[f"{col}"].mean()
        filtered_sell[f'Avg{col}My'] = col_mean

    # 기존 컬럼 탈락
    filtered_sell.drop(columns=[cols, "age"])

    # 2. Buy
    # 우리아이 나이대 평균
    for col in cols:
        col_mean = buy[f"{col}"].mean()
        buy[f'Avg{col}Age'] = col_mean
    
    # 우리아이 평균
    filtered_buy = buy[buy["userId"] == userId]

    for col in cols:
        my_mean = filtered_buy[f"{col}"].mean()
        filtered_buy[f'Avg{col}My'] = col_mean
    
    # 기존 컬럼 탈락
    filtered_buy.drop(columns=[cols, "age"])


    # 3. Sell Buy 병합
    df = pd.concat([filtered_sell, filtered_buy], axis=0, ignore_index=True)
    
    return df



def make_df_graph3(userId):
    df = load_df()

    df1 = bet_buy_ratio(df)
    df1 = filtered_mean(df1, "betBuyRatio", userId)

    df2 = bet_sell_ratio(df)
    df2 = filtered_mean(df2, "betSellRatio", userId)

    fin_df = pd.merge(df1, df2, on="investSessionId", how="outer")

    return fin_df

def make_df_graph4(userId):
    df = load_df()

    df = avg_cash_ratio(df)
    df = filtered_mean(df, "avgCashRatio", userId)

    return df