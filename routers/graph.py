from fastapi import APIRouter
from utils.make_graph import make_df_graph1, make_df_graph2_1, make_df_graph2_2, make_df_graph2_3, make_df_graph3, make_df_graph4

router = APIRouter(prefix="/api/graph")

@router.get("/graph1/all")
def graph1(userId :str):
    df = make_df_graph1(userId)
    return df.to_dict(orient="records")

@router.get("/graph1/week")
def graph1(userId :str):
    df = make_df_graph1(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/1/all")
def graph2_1(userId :str):
    df = make_df_graph2_1(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/1/week")
def graph2_1(userId :str):
    df = make_df_graph2_1(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/2/all")
def graph2_2(userId :str):
    df = make_df_graph2_2(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/2/week")
def graph2_2(userId :str):
    df = make_df_graph2_2(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/3/all")
def graph2_3(userId :str):
    df = make_df_graph2_3(userId)
    return df.to_dict(orient="records")

@router.get("/graph2/3/week")
def graph2_3(userId :str):
    df = make_df_graph2_3(userId)
    return df.to_dict(orient="records")

@router.get("/graph3/all")
def graph3(userId :str):
    df = make_df_graph3(userId)
    return df.to_dict(orient="records")

@router.get("/graph3/week")
def graph3(userId :str):
    df = make_df_graph3(userId)
    return df.to_dict(orient="records")

@router.get("/graph4/all")
def graph4(userId :str):
    df = make_df_graph4(userId)
    return df.to_dict(orient="records")

@router.get("/graph4/week")
def graph4(userId :str):
    df = make_df_graph4(userId)
    return df.to_dict(orient="records")