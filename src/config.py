import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(str(Path(".bot.env").resolve()))

VK_API_KEY = os.getenv("VK_API_KEY", "")
