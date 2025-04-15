import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://forfunsake04:VuMLpQZ9hI5i6ua3@fsuplayers.nzbrr8s.mongodb.net/")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.fsu_dashboard
