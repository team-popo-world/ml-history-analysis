import pandas as pd
from db.merge_df import load_df
from utils.avg_stay_time import avg_stay_time
from utils.tag_avg_stay_time import tag_avg_stay_time
from utils.filtered_mean import filtered_mean
from utils.bet_buy_ratio import bet_buy_ratio
from utils.bet_sell_ratio import bet_sell_ratio
from utils.avg_cash_ratio import avg_cash_ratio

def make_graph1(userId):
    df = load_df()

    df1 =avg_stay_time(df)
    df1 = filtered_mean(df1, "avgStayTime", userId)

    df2 = tag_avg_stay_time(df)
    df2 = filtered_mean(df2, "tagAvgStayTime", userId)

    fin_df = pd.merge(df1, df2, on="investSessionId", how="outer")

    return fin_df

def make_graph2(userId):
    df = load_df()

    graph2_1()
    graph2_2()
    graph2_3()

    return df

def make_graph2_1(userId):
    return df

def make_graph2_2(userId):

    return df

def graph2_3(userId):

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