import requests
import json


# Define the API endpoint and parameters
url = "http://api.football-data.org/v2/competitions/2021/standings"
headers = {
    "X-Auth-Token": "10f2ddeaeeac480084b8b62a05a8bdd6" # replace with your own API key
}

# Send a GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check if the response was successful (HTTP status code 200)
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()

    # Extract the team standings from the response
    standings = data["standings"][0]["table"]

    # Print the team standings
    for team in standings:
        print(f"{team['position']}. {team['team']['name']}: {team['points']} points")
else:
    print(f"Error: {response.status_code}")
