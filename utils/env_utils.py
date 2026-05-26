import os

from dotenv import load_dotenv

load_dotenv(override=True)

# mcp相关
COOKIES_STR = os.getenv("COOKIES_STR")
