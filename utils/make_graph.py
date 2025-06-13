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

    Sell = ["highSellRatio","midSellRatio","lowSellRatio"]
    Buy = ["highBuyRatio","midBuyRatio","lowBuyRatio"]

    all_types = [("Sell", Sell), ("Buy", Buy)]
    
    # 우리 아이랑 같은 나이를 갖는 행만 필터링
    child_age = df.loc[df["childId"]==userId, "age"].iloc[0] 
    df = df[df["age"] == child_age].copy()
    for label, col_list in all_types:
        for col in col_list:
            # 우리아이 나이대 평균
            col_mean = df[f"{col}"].mean()
            new_col = col.replace(label, "")
            df[f'{new_col}_age'] = col_mean
        df['Type'] = label

    # 우리아이 평균
    filtered_df = df[df["userId"] == userId]

    for label, col_list in all_types:
        for col in col_list:
            my_mean = filtered_df[f"{col}"].mean()
            new_col = col.replace(label, "")
            filtered_df[f'My{col}Mean'] = my_mean
        filtered_df['Type'] = label

    # age drop
    filtered_df.drop(columns="age", inplace=True)
    
    return filtered_df

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