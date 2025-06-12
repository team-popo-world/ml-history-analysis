from db.mongo_handler import load_mongo_data
from db.postgres_handler import load_postgres_data
from utils.preprocess import mongo_preprocess
from utils.trading_turn import trading_turn
from utils.transaction_num import transaction_num
from utils.avg_cash_ratio import avg_cash_ratio
from utils.avg_stay_time import avg_stay_time
from utils.avg_trade_ratio import avg_trade_ratio
from utils.tag_avg_stay_time import tag_avg_stay_time

# MongoDB
mongo_df = load_mongo_data()
mongo_df = mongo_preprocess(mongo_df)

# PostgreSQL
seed_df, user_df = load_postgres_data()

# Preprocessing
tradingTurn = trading_turn(mongo_df)
transactionNum = transaction_num(mongo_df)
avgCashRatio = avg_cash_ratio(mongo_df, seed_df)
avgStayTime = avg_stay_time(mongo_df)
avgTradeRatio = avg_trade_ratio(mongo_df)
tagAvgStayTime = tag_avg_stay_time(mongo_df)

# 결과 출력
print(mongo_df.head())
print("#################################")
print(seed_df.head())
print("#################################")
print(user_df.head())

merged = tradingTurn.merge(transactionNum, on='investSessionId', how='inner').merge(avgCashRatio, on='investSessionId', how='inner').merge(avgStayTime, on='investSessionId', how='inner') #.merge(avgTradeRatio, on='investSessionId', how='inner') #.merge(tagAvgStayTime, on='investSessionId', how='inner').merge(riskTaking, on='investSessionId', how='inner')
print("#################################")
print(merged.head())
