from fastapi import APIRouter
from utils.make_graph import make_df_graph1, make_df_graph2_1, make_df_graph2_2, make_df_graph2_3, make_df_graph3, make_df_graph4

router = APIRouter(prefix="/api/graph")

@router.get("/graph1")
def graph1(userId :str):
    df = make_df_graph1(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/1")
def graph2_1(userId :str):
    df = make_df_graph2_1(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/2")
def graph2_2(userId :str):
    df = make_df_graph2_2(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/3")
def graph2_3(userId :str):
    df = make_df_graph2_3(userId)
    return df.to_dict(orient="records")

@router.get("/graph3")
def graph3(userId :str):
    df = make_df_graph3(userId)
    return df.to_dict(orient="records")

@router.get("/graph4")
def graph4(userId :str):
    df = make_df_graph4(userId)
    return df.to_dict(orient="records")