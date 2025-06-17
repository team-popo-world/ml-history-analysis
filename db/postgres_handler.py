import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)

# snake_case -> camelCase
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def load_postgres_data(query: str):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    # seed_query = "SELECT chapter_id, seed_money FROM invest_chapter ;"
    # user_query = "SELECT user_id, sex, age FROM users;"

    # seed_df = pd.read_sql(seed_query, conn)
    # user_df = pd.read_sql(user_query, conn)

    df = pd.read_sql(query, conn)

    conn.close()

    df.columns = [snake_to_camel(col) for col in df.columns]
    # seed_df.rename(columns={'chapter_id': 'chapterId'}, inplace=True)
    # seed_df.rename(columns={'seed_money': 'seedMoney'}, inplace=True)
    # seed_df.columns = [snake_to_camel(col) for col in seed_df.columns]
    # user_df.columns = [snake_to_camel(col) for col in user_df.columns]
    # user_df.rename(columns={'user_id':'userId'}, inplace=True)

    return df