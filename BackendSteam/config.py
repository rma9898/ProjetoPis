from dotenv import load_dotenv
import os

# Informações de acesso à API
load_dotenv()
API_URL = os.getenv("API_URL")
STEAM_URL = os.getenv("STEAM_URL")