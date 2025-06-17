from db.merge_df import load_df
from utils.trading_turn import trading_turn
from utils.transaction_num import transaction_num
from utils.avg_cash_ratio import avg_cash_ratio
from utils.avg_stay_time import avg_stay_time
from utils.avg_trade_ratio import avg_trade_ratio
from utils.tag_avg_stay_time import tag_avg_stay_time
from utils.bet_buy_ratio import bet_buy_ratio
from utils.bet_sell_ratio import bet_sell_ratio
from utils.bet_shares import bet_shares
from models.RandomForest import random_forest, rf_predict_invest_type

df = load_df()
print(df.head())

# Preprocessing
userInfo = df[['userId', 'sex', 'age']].copy()
print("#########3UserInfo##########", userInfo)
tradingTurn = trading_turn(df)
transactionNum = transaction_num(df)
avgCashRatio = avg_cash_ratio(df)
avgStayTime = avg_stay_time(df)
# print(avgStayTime.head())
avgTradeRatio = avg_trade_ratio(df)
tagAvgStayTime = tag_avg_stay_time(df)
# print(tagAvgStayTime.head())
betBuyRatio = bet_buy_ratio(df)
# print(betBuyRatio.head())
betSellRatio = bet_sell_ratio(df)
# print(betSellRatio.head())
betShares = bet_shares(df)
# print(betShares.head())

# 결과 출력
# print(mongo_df.head())
# print("#################################")
# print(seed_df.head())
# print("#################################")
# print(user_df.head())

# merged = tradingTurn.merge(transactionNum, on='investSessionId', how='inner').merge(avgCashRatio, on='investSessionId', how='inner').merge(avgStayTime, on='investSessionId', how='inner') #.merge(avgTradeRatio, on='investSessionId', how='inner') #.merge(tagAvgStayTime, on='investSessionId', how='inner').merge(riskTaking, on='investSessionId', how='inner')
# print("#################################")
# print(merged.head())

# final_data = merged.merge(userInfo, on='userId', how="inner")

# rf_predict_invest_type(final_data)