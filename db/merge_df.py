import pandas as pd
from db.mongo_handler import load_mongo_data
from db.postgres_handler import load_postgres_data
from utils.preprocess import mongo_preprocess

def load_df():
    # MongoDB
    mongo_df = load_mongo_data()
    mongo_df = mongo_preprocess(mongo_df)
    print("laod_df내부에 있는 mongo_db", mongo_df.head())
    print("load_df 내부에 있는 mongo_df columns:", mongo_df.columns.tolist())

    # PostgreSQL
    seed_df, user_df = load_postgres_data()
    print("laod_df내부에 있는 seed_df", seed_df.head())
    print("laod_df내부에 있는 user_df", user_df.head())

    merge = mongo_df.merge(seed_df, on="chapterId", how="inner")
    print("laod_df내부에 있는 seed + mongo", merge.head())
    merged_df = merge.merge(user_df, on="userId", how="inner")

    return merged_df
