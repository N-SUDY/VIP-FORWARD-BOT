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
    SESSION = os.environ.get("SESSION", "BQAu8HnWatwHa3606F4XRUkBvFwlsx21TwHR_Q8_p6xeOISNYUDLMqqWkxdOBexK0fl7dcLu5mqFbUNwFyyCtnROsrCZ_xKWO545jR8flIX3yi_k2WxN-sHLLEfwucY0m2rKozoGnWMkJ5OmVHJSh6EOXgRJeDf9sOdtXfFBVRTOf8k_t7_huU_aX5TJ2BSLdNkqkCwUrrtGLS_7Clm2fX4ki2XODzHKPLk0gzqA-8JYm8kbfkWEr7E16v1UKEOivCvG5Gv8H8IeRsTkk3e2BbZHug4bp7ismkrxh8GS4O-YKTvGysYMo7YFeZZ6lJ9Tv87rgqgtajIWkZOiL6pu24AAAAAWmJoYoA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001946118544"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "VIP_FORWARD_ROBOT")
    PORT = os.environ.get("PORT", "8080")
    WEBHOOK = bool(os.environ.get("WEBHOOK", True)) # for web support on/off


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
