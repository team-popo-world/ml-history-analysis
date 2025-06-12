import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(override=True)

def load_mongo_data():
    # MongoDB 연결 정보
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB_NAME")
    collection_name = os.getenv("COLLECTION_NAME")

    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]

    df = pd.DataFrame(list(collection.find()))

    ### 나중에 삭제될 코드 ###
    df.rename(columns={'childId': 'userId'}, inplace=True)
    ########################

    df['riskLevel'] = df['riskLevel'].replace({
        '고위험 고수익': 'high',
        '균형형': 'mid',
        '장기 안정형': 'low'
    })

    df.sort_values(by=['investSessionId', 'riskLevel', 'turn'], inplace=True)
    df['deltaShares'] = df.groupby(['investSessionId', 'riskLevel'])['numberOfShares'].diff()
    df['deltaShares'] = df['deltaShares'].fillna(df['numberOfShares'])
    df['deltaShares'] = df['deltaShares'].astype(int)
    
    return df