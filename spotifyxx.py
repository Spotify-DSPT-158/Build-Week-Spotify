import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Load .env credentials
load_dotenv()

# Spotify Credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
client_URI = os.getenv('CLIENT_REDIRECT_URI')

# Create spotifyObject
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
results = sp.search(q='garth brooks', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

# Get username from the terminal
# username = sys.argv[1]

# In order to get your spotify id you need to do the following:
# - log into your spotify account
# - click your picture, which will take you to your account overview
# - there you will see your username, which is a list of numbers,
#   if you created your account through Facebook, or your actual
#   username, if you created your account directly through spotify

# token = util.prompt_for_user_token(username, client_id,
#                                    client_secret, client_URI)

# except:
#     os.remove(f'.cache-{username}')
#     token = util.prompt_for_user_token(username, client_id,
#                                        client_secret, client_URI)

# Need to go back to terminal and enter:
#   `export SPOTIPY_CLIENT_ID='<enter your client id>' (if using bash)
#   `set SPOTIPY_CLIENT_ID='<enter your client id>' (if using windows cmd)
#   `export SPOTIPY_CLIENT_SECRET='<enter your secret id>' (if using bash)
#   `set SPOTIPY_CLIENT_SECRET='<enter your secret id>' (if using windows cmd)
#   `export SPOTIPY_REDIRECT_URI='<enter your URI>' (if using bash)
#   `set SPOTIPY_REDIRECT_URI='<enter your URI>' (if using windows cmd)

# Need to run it to verify everything is working:
# - In the terminal: `python spotifyxx.py <your username>`
#   ^-- Could not get this to work.
