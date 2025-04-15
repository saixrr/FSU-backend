from fastapi import APIRouter, HTTPException
from app.models.player_game import PlayerGame
from app.database import db
from typing import List

router = APIRouter()

# GET all game stats (limit 100 for now)
@router.get("/player-games", response_model=List[PlayerGame])
async def get_player_games():
    games = await db.player_games.find().to_list(100)
    return games

# POST a new player game stat entry
@router.post("/player-games")
async def add_player_game(player_game: PlayerGame):
    result = await db.player_games.insert_one(player_game.dict())
    return {"id": str(result.inserted_id), "message": "Game entry added successfully"}
