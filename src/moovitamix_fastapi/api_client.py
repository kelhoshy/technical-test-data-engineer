from fastapi.testclient import TestClient
from main import app  

class APIClient:
    def __init__(self, url: str, port: int, route: str):
        #Initialize the APIClient with the FastAPI TestClient and a specific route.
        
        self.client = TestClient(app) 
        self.url = url
        self.port = port
        self.route = route

    def get_data(self):
        #Fetch data from the FastAPI route provided during initialization.
        
        response = self.client.get(f"/{self.route}")
        if response.status_code == 200:
            return response.json()  # Return the parsed JSON data
        else:
            print(f"Failed to fetch data from {self.route}: {response.status_code}")
            return None