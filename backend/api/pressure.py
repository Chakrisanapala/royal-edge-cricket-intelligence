from fastapi import APIRouter
from backend.services.data_service import data_service

router = APIRouter(prefix="/api/pressure", tags=["Pressure Intelligence"])

@router.get("/summary")
def get_pressure_summary():
    return data_service.get_pressure_summary()

