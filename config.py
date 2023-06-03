import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21288218"))
    API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6021415198:AAGJ5z8r-bBK9iXzvymHHoKywAW-TDEPzCY")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6065594762")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://FORWARD:FORWARD@cluster0.k1omlka.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCznnlV6c0lNK7OTC9wL5VvXOcg2fbnESgAK83hWNAn5FBPx5ahahh7OEk3GVsl5RzV-Aye2pbBzV7b4e8IRJgAj4gfNaWutldH7sT50KFLjTbKHIm7_lFJEIhMswxnOhNo40qOScjy3OSEXpBYFCRypeYp1ts2d07LLOapYP_0PGeYlg3oH0mG9JR-lveuQ6AnlysDS8VDvX57DxvZFzfSojKjW-qG3soS4oRNsUwLOEhm5ddsrKHEiaoredjpaX9e78dopf_CSC1HmmsuBaffHiqACl7uJoYkxDM0rLL45WTGKAyxDoRS88ipgG4mMhmNbj0OlZWl-KQapkBmeKTiAAAAAWmJoYoA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001946118544"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")
    PORT = os.environ.get("PORT", "8080")
    WEBHOOK = bool(os.environ.get("WEBHOOK", True)) # for web support on/off


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
