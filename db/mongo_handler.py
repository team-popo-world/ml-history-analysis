import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.binary import Binary
import uuid

load_dotenv(override=True)

collection_map = {
    "invest": os.getenv("INVEST_HISTORY"),
    "quest": os.getenv("QUEST_HISTORY"),
    "saving_account": os.getenv("SAVING_ACCOUNT_HISTORY"),
}

# Binary UUID를 문자열로 변환하는 함수
def binary_to_uuid_string(binary_uuid):
    if isinstance(binary_uuid, Binary):
        return str(uuid.UUID(bytes=binary_uuid))
    return binary_uuid

# 불러온 mongoDB 전처리
def mongo_preprocess(df):
    # childId(또는 userId) 컬럼의 Binary를 문자열 UUID로 변환
    """
    if 'childId' in df.columns:
        df['childId'] = df['childId'].apply(binary_to_uuid_string)
        df.rename(columns={'childId':'userId'}, inplace=True)
    elif 'userId' in df.columns:
        df['userId'] = df['userId'].apply(binary_to_uuid_string)
    """
    if 'userId' in df.columns:
        df['userId'] = df['userId'].apply(binary_to_uuid_string)

    if 'riskLevel' in df.columns:
        df['riskLevel'] = df['riskLevel'].replace({
            '고위험 고수익': 'high',
            '균형형': 'mid',
            '장기 안정형': 'low'
        })

    if all(col in df.columns for col in ['investSessionId', 'riskLevel', 'turn']):
        df.sort_values(by=['investSessionId', 'riskLevel', 'turn'], inplace=True)
        df['deltaShares'] = df.groupby(['investSessionId', 'riskLevel'])['numberOfShares'].diff()
        df['deltaShares'] = df['deltaShares'].fillna(df['numberOfShares'])
        df['deltaShares'] = df['deltaShares'].astype(int)

    return df

def load_mongo_data(fields=None, collection: str = "invest"):
    # MongoDB 연결 정보
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB_NAME")
    # collection_name = os.getenv("COLLECTION_NAME")
    collection_name = collection_map[collection]

    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]

    # fields 리스트를 projection 딕셔너리로 변환
    projection = {field: 1 for field in fields} if fields else None
    if projection is not None:
        projection['_id'] = 0  # 기본적으로 _id는 제외

    df = pd.DataFrame(list(collection.find({}, projection)))
    df = mongo_preprocess(df)

    return df