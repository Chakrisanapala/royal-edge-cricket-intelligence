from fastapi import APIRouter
from backend.services.data_service import data_service

router = APIRouter(prefix="/api/overview", tags=["Overview"])

@router.get("")
def get_overview():
    return data_service.get_overview()

