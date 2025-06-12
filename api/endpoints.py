from fastapi import APIRouter
from db.mongo_handler import load_mongo_data
from db.postgres_handler import load_postgres_data
from utils.preprocess import preprocess_mongo_data

router = APIRouter()

@router.get("/data")
def get_processed_data():
    mongo_df = load_mongo_data()
    processed_df = preprocess_mongo_data(mongo_df)
    return processed_df.to_dict(orient="records")