from fastapi import APIRouter, HTTPException
from app.models.player_game import PlayerGame
from app.database import db
from typing import List
from fastapi import Query
from typing import Optional

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

@router.get("/player-games/filter", response_model=List[PlayerGame])
async def filter_player_games(
    name: Optional[str] = Query(None),
    position: Optional[str] = Query(None),
    year: Optional[str] = Query(None),
    opponent: Optional[str] = Query(None),
    gameType: Optional[str] = Query(None),
    statCategory: Optional[str] = Query(None),
):
    filters = {}

    if name:
        filters["playerName"] = {"$regex": name, "$options": "i"}

    if position and position != "ALL":
        filters["position"] = position

    if year and year != "ALL":
        filters["season"] = year

    if opponent and opponent != "ALL":
        filters["opponent"] = opponent

    if gameType and gameType != "ALL":
        filters["gameType"] = gameType

    if statCategory and statCategory != "ALL":
        if statCategory == "Passing":
            filters["passingYards"] = {"$gt": 0}
        elif statCategory == "Rushing":
            filters["rushingYards"] = {"$gt": 0}
        elif statCategory == "Receiving":
            filters["receivingYards"] = {"$gt": 0}
        elif statCategory == "Defense":
            filters["$or"] = [
                {"tackles": {"$gt": 0}},
                {"sacks": {"$gt": 0}},
                {"interceptions": {"$gt": 0}}
            ]
        elif statCategory == "Kicking":
            filters["$or"] = [
                {"fieldGoalsMade": {"$gt": 0}},
                {"extraPointsMade": {"$gt": 0}}
            ]

    games = await db.player_games.find(filters).to_list(1000)
    return games