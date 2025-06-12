import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(override=True)

def load_mongo_data(fields=None):
    # MongoDB 연결 정보
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB_NAME")
    collection_name = os.getenv("COLLECTION_NAME")

    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]

    # projection 설정
    if fields:
        projection = {field: 1 for field in fields}
        projection['_id'] = 0  # _id는 제외
    else:
        projection = None  # 전체 컬럼 가져옴

    df = pd.DataFrame(list(collection.find({}, projection)))

    return df