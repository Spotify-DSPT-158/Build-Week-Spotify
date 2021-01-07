import os
import pickle
import pandas

basedir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(basedir, model.pkl)
df_path = os.path.join(basedir, ## Pickle Path)

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(df_path, 'rb') as f:
    df = pickle.load(f)

def find_recommended_songs(track_id):
    song_index = df.index[df['id'] == track_id]
    audio_features = df.iloc[song_index, 3:].to_numpy()
    distances, indices = model.kneighbors(audio_features)
    return df.iloc[indices[0], 'id'].tolist()

def track_id_in_df(track_id):
    return len(df.index[df['id'] == track_id])> 0
