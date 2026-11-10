from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from backend.services.data_service import data_service

router = APIRouter(prefix="/api/auction", tags=["Auction War Room"])

class AuctionSimulateRequest(BaseModel):
    remaining_purse: float = 42.80
    bids: Dict[str, float]

@router.get("/targets")
def get_auction_targets():
    return data_service.get_auction_targets()

@router.post("/simulate")
def simulate_auction(req: AuctionSimulateRequest):
    return data_service.simulate_auction(req.remaining_purse, req.bids)

