from db.mongo_handler import load_mongo_data
from db.postgres_handler import load_postgres_data

def load_df(col: list = None, collection: str = "invest",  use_seed: bool = False):
    # MongoDB
    mongo_df = load_mongo_data(col, collection)

    # PostgreSQL
    seed_df, user_df = load_postgres_data()

    if use_seed:
        merge = mongo_df.merge(seed_df, on="chapterId", how="inner")
    else:
        merge = mongo_df.copy()
    
    merged_df = merge.merge(user_df, on="userId", how="inner")

    return merged_df

### 각 모듈의 출력값 ###
### investSessionId, userId, age, 각 집계값, startedAt은 필수로 나와야함 ###