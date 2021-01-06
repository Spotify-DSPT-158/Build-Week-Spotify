import os
import pickle
import pandas

basedir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(basedir, ##insert model)
df_path = os.path.join(basedir, ## Pickle Path)

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(df_path, 'rb') as f:
    df = pickle.load(f)

def find_recommended_songs(track_id):
    song_index = df.index[df['id'] == track_id]
    audio_features = df