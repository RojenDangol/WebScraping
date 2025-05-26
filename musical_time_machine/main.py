import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="https://example.com/callback",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

travel_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_year}/"

response = requests.get(URL, headers=headers)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
songs = soup.select(selector="li ul li h3")

song_names = [song.getText().strip() for song in songs]

song_uris = []
year = travel_year.split("-")[0]

playlist = sp.user_playlist_create(user=user_id, name=f"{travel_year} Billboard 100", public=False)
playlist_id = playlist["id"]

for song in song_names:
    results = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(results)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. SKipped.")


# for uri in song_uris:
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)