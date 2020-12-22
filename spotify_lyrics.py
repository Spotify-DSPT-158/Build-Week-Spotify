import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load .env credentials
load_dotenv()

# Spotify Credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
client_URI = os.getenv('CLIENT_REDIRECT_URI')

# Create spotifyObject
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
results = sp.search(q='george straight', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])