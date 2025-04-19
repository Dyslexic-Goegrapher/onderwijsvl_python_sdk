import requests
import json
import os

from main import OnderwijsVlaanderenAPI
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Instellingen(OnderwijsVlaanderenAPI):
    def __init__(self, domain: str = "https://onderwijs.api.vlaanderen.be", path: str = "instellingsgegevens/instelling/v2/instelling", api_key: Optional[str] = None):
        self.api_key = os.getenv("API_KEY")
        super().__init__(api_key=self.api_key, domain=domain)
        self.url = f"{domain}/{path}"

        response = requests.get(self.url, params=self.params, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f"Failed to connect to the API: {response.status_code} - {response.text}")
        
        self.data = response.json()
        if not self.data:
            raise ValueError("No data found in the response")
    

if __name__ == "__main__":
    try:
        instellingen = Instellingen()
        print(json.dumps(instellingen.data, indent=4))
    except Exception as e:
        print(f"Error: {e}")    
