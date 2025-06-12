from db.mongo_handler import load_mongo_data
from db.postgres_handler import load_postgres_data
from utils.preprocess import trading_turn, transaction_num, avg_cash_ratio, avg_stay_time

# MongoDB
mongo_df = load_mongo_data()

# PostgreSQL
seed_df, user_df = load_postgres_data()

# Preprocessing
tradingTurn = trading_turn(mongo_df)
transactionNum = transaction_num(mongo_df)
avgCashRatio = avg_cash_ratio(mongo_df, seed_df)
avgStayTime = avg_stay_time(mongo_df)

# 결과 출력
print(mongo_df.head())
print("#################################")
print(seed_df.head())
print("#################################")
print(user_df.head())

merged = tradingTurn.merge(transactionNum, on='investSessionId', how='inner').merge(avgCashRatio, on='investSessionId', how='inner').merge(avgStayTime, on='investSessionId', how='inner') #.merge(avgTradeRatio, on='investSessionId', how='inner') #.merge(tagAvgStayTime, on='investSessionId', how='inner').merge(riskTaking, on='investSessionId', how='inner')
print("#################################")
print(merged.head())
