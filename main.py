from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variable from the .env file
load_dotenv("./vars/.env")

SPOTIFY_CLIENT = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")

# Authenticate with Spotify using OAuth
"""User will have to login to their spotify and paste the URL in the console"""
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        # Cache the token to avoid re-authentication
        cache_path="token.txt",
        username="Alvin C",
    )
)
# Get the authenticated user's ID
user_id = sp.current_user()["id"]


# Function to check if user input is in the correct date format (YYYY-MM-DD)
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Loop until the user provides a valid date
while True:
    userPrompt = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    if is_valid_date(userPrompt):
        break
    else:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Fetch the 100 top charts from billboard
response = requests.get(f"https://www.billboard.com/charts/hot-100/{userPrompt}/")
billboard_hot = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(billboard_hot, "html.parser")

# Find all the tag that has the top 100 song
span_tags = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in span_tags]
print(song_names)

# List to store Spotify URIs for the songs
song_uris = []
year = userPrompt.split("-")[0] # Extract the year from the user input

# Search for each song on Spotify and get its URI
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new Spotify playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{userPrompt} Billboard 100", public=False)
print(playlist)

# Add the songs to the newly created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)