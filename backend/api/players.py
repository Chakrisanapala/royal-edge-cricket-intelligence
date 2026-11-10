from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from backend.services.data_service import data_service

router = APIRouter(prefix="/api/players", tags=["Players"])

@router.get("/batters")
def get_batters(
    role: Optional[str] = Query(None, description="Batting role filter"),
    search: Optional[str] = Query(None, description="Search by name or team"),
    sort_by: str = Query("bpri_score", description="Sort field"),
    ascending: bool = Query(False, description="Ascending order")
):
    return data_service.get_batters(role=role, search=search, sort_by=sort_by, ascending=ascending)

@router.get("/bowlers")
def get_bowlers(
    actionable_only: bool = Query(False, description="Filter for BCCI-eligible actionable targets"),
    search: Optional[str] = Query(None, description="Search by name or team"),
    sort_by: str = Query("bowpri_score", description="Sort field"),
    ascending: bool = Query(False, description="Ascending order")
):
    return data_service.get_bowlers(actionable_only=actionable_only, search=search, sort_by=sort_by, ascending=ascending)

@router.get("/{player_id}")
def get_player(player_id: int):
    profile = data_service.get_player_profile(player_id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"Player with ID {player_id} not found")
    return profile

