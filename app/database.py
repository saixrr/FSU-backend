import motor.motor_asyncio
import os
from dotenv import load_dotenv

from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

print("LOADED:", os.getenv("MONGO_URI"))  # should now show Atlas URI


MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://forfunsake04:VuMLpQZ9hI5i6ua3@fsuplayers.nzbrr8s.mongodb.net/")
print("Loaded MONGO_URI:", os.getenv("MONGO_URI"))


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.fsu_dashboard
