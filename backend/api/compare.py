from fastapi import APIRouter, HTTPException, Query
from backend.services.data_service import data_service

router = APIRouter(prefix="/api/compare", tags=["Player Comparison"])

@router.get("")
def compare_players(
    player_a_id: int = Query(..., description="First player ID"),
    player_b_id: int = Query(..., description="Second player ID"),
    player_type: str = Query("batter", description="'batter' or 'bowler'")
):
    result = data_service.compare_players(player_a_id, player_b_id, ptype=player_type)
    if not result:
        raise HTTPException(status_code=400, detail="Invalid player IDs or player type")
    return result

