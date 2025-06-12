from fastapi import APIRouter

router = APIRouter(prefix="/api/cluster")

@router.get("/invest")
def invest():
    return {"message": "투자 클러스터링"}