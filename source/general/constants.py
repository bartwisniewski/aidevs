import os

from dotenv import load_dotenv
load_dotenv()


SERVER = "https://zadania.aidevs.pl"
API_KEY = os.getenv("API_KEY")
OPENAI_KEY = os.getenv("OPENAI_KEY")
