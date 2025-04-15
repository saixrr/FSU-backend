# app/models/player_game.py
from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class PlayerGame(BaseModel):
    playerName: str
    playerPhoto: Optional[str] = None
    position: Literal['QB', 'RB', 'WR', 'TE', 'OL', 'DL', 'LB', 'CB', 'S', 'K', 'P']
    opponent: str
    gameType: Literal['regular', 'conference', 'non-conference', 'playoff', 'bowl']
    location: Literal['Home', 'Away', 'Neutral']
    date: datetime
    season: str
    result: Optional[str] = None

    passingYards: Optional[int] = 0
    passingTDs: Optional[int] = 0
    passingInt: Optional[int] = 0
    rushingYards: Optional[int] = 0
    rushingTDs: Optional[int] = 0
    receptions: Optional[int] = 0
    receivingYards: Optional[int] = 0
    receivingTDs: Optional[int] = 0
    tackles: Optional[int] = 0
    sacks: Optional[float] = 0.0
    interceptions: Optional[int] = 0
