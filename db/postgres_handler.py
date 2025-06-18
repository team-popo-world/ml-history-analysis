import os
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv(override=True)

# snake_case -> camelCase
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def load_postgres_data(query: str):
    host=os.getenv("DB_HOST")
    port=os.getenv("DB_PORT")
    dbname=os.getenv("DB_NAME")
    user=os.getenv("DB_USER")
    password=quote_plus(os.getenv("DB_PASSWORD"))

    engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    )

    # seed_query = "SELECT chapter_id, seed_money FROM invest_chapter ;"
    # user_query = "SELECT user_id, sex, age FROM users;"

    # seed_df = pd.read_sql(seed_query, conn)
    # user_df = pd.read_sql(user_query, conn)

    df = pd.read_sql(query, engine)

    df.columns = [snake_to_camel(col) for col in df.columns]
    # seed_df.rename(columns={'chapter_id': 'chapterId'}, inplace=True)
    # seed_df.rename(columns={'seed_money': 'seedMoney'}, inplace=True)
    # seed_df.columns = [snake_to_camel(col) for col in seed_df.columns]
    # user_df.columns = [snake_to_camel(col) for col in user_df.columns]
    # user_df.rename(columns={'user_id':'userId'}, inplace=True)

    return df