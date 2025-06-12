from fastapi import APIRouter

router = APIRouter(prefix="/api/graph")

@router.get("/graph1")
def graph1():
    return {"message": "요약 데이터1"}

@router.get("/graph2")
def graph2():
    return {"message": "요약 데이터2"}

@router.get("/graph3")
def graph3():
    return {"message": "요약 데이터3"}

@router.get("/graph4")
def graph4():
    return {"message": "요약 데이터4"}