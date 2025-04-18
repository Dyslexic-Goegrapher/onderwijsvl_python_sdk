import requests
from typing import Optional
from dotenv import load_dotenv
import os
from logging import getLogger

load_dotenv()
logger = getLogger(__name__)

class OnderwijsVlaanderenAPI:
    def __init__(self, base_url: str = "https://onderwijs.api.vlaanderen.be", api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Set it as an environment variable or pass it directly")

        self.params = {
            "api_key": self.api_key
        }
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.session = requests.Session()  # Reuse the session for performance
        self.session.headers.update(self.headers)
