import os
from logging import getLogger

logger = getLogger(__name__)

class OnderwijsVlaanderenAPI:
    def __init__(self, api_key: str, domain: str = "https://onderwijs.api.vlaanderen.be"):
        self.domain = domain
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("API key is required. Set it as an environment variable or pass it directly")

        self.params = {
            "apikey": self.api_key
        }
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
