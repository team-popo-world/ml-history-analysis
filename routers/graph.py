from fastapi import APIRouter
from db.merge_df import load_df
from utils.make_graph import make_df_graph1, make_df_graph2, make_df_graph3, make_df_graph4

router = APIRouter(prefix="/api/graph")

@router.get("/graph1")
def graph1(userId):
    df = make_df_graph1(userId)
    return df.to_dict(orient="records")

@router.get("/graph2")
def graph2(userId):
    df = make_df_graph2(userId)
    return df.to_dict(orient="records")

@router.get("/graph3")
def graph3(userId):
    df = make_df_graph3(userId)
    return df.to_dict(orient="records")

@router.get("/graph4")
def graph4(userId):
    df = make_df_graph4(userId)
    return df.to_dict(orient="records")