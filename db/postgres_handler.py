import os
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv(override=True)

def load_postgres_data():
    host=os.getenv("DB_HOST")
    port=os.getenv("DB_PORT")
    dbname=os.getenv("DB_NAME")
    user=os.getenv("DB_USER")
    password=quote_plus(os.getenv("DB_PASSWORD"))

    engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    )
    
    seed_query = "SELECT chapter_id, seed_money FROM invest_chapter ;"
    user_query = "SELECT user_id, sex, age FROM users;"

    seed_df = pd.read_sql(seed_query, engine)
    user_df = pd.read_sql(user_query, engine)

    seed_df.rename(columns={'chapter_id': 'chapterId'}, inplace=True)
    seed_df.rename(columns={'seed_money': 'seedMoney'}, inplace=True)

    user_df.rename(columns={'user_id':'userId'}, inplace=True)

    return seed_df, user_df