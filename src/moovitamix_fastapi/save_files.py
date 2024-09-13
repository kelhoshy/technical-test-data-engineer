import json
from api_client import APIClient

def save_data_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    user_client = APIClient("http://localhost", 8000, "users")
    track_client = APIClient("http://localhost", 8000, "tracks")
    history_client = APIClient("http://localhost", 8000, "listen_history")
    top_client = APIClient("http://localhost", 8000, "top_songs")
    
    users = user_client.get_data()
    tracks = track_client.get_data()
    listen_history = history_client.get_data()
    top_songs = top_client.get_data()

    #Assuming that you want to collect all the data in the same file
    consolidated_data = {
        "users": users,
        "tracks": tracks,
        "listen_history": listen_history
    }
    

    save_data_to_file(consolidated_data, "all_data.json")