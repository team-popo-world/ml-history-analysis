import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)

def load_postgres_data():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    seed_query = "SELECT chapter_id, seed_money FROM invest_chapter ;"
    user_query = "SELECT user_id, sex, age FROM users;"

    seed_df = pd.read_sql(seed_query, conn)
    user_df = pd.read_sql(user_query, conn)

    conn.close()

    seed_df.rename(columns={'chapter_id': 'chapterId'}, inplace=True)
    seed_df.rename(columns={'seed_money': 'seedMoney'}, inplace=True)

    user_df.rename(columns={'user_id':'userId'}, inplace=True)

    return seed_df, user_df