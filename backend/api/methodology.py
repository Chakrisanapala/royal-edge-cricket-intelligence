from fastapi import APIRouter
from backend.services.data_service import data_service

router = APIRouter(prefix="/api/methodology", tags=["Methodology"])

@router.get("")
def get_methodology():
    return data_service.get_methodology()

