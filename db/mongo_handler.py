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

    df = pd.DataFrame(list(collection.find()))

    return df