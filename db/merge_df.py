import pandas as pd
from db.mongo_handler import load_mongo_data
from db.postgres_handler import load_postgres_data
from utils.preprocess import mongo_preprocess

def load_df():
    # MongoDB
    mongo_df = load_mongo_data()
    mongo_df = mongo_preprocess(mongo_df)
    print(mongo_df.head())

    # PostgreSQL
    seed_df, user_df = load_postgres_data()
    print(seed_df.head())
    print(user_df.head())

    merge = mongo_df.merge(seed_df, on="chapterId", how="inner")
    print(merge.head())
    print(merge.info())
    merged_df = merge.merge(user_df, on="userId", how="inner")
    print(merged_df.info())
    print(merged_df.head())

    return merged_df