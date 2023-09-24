import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()
# your app code here
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
con = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id,
                                                              client_secret = client_secret))
artist_id = "75U40yZLLPglFgXbDVnmVs"
response = con.artist_top_tracks(artist_id)
tracks = response["tracks"]
for track in tracks:
    print('track    : ' + track['name'])
    print()

tracks_df = pd.DataFrame.from_records(tracks)
print(tracks_df.info())
tracks_df.sort_values(("popularity"), inplace=True)
print(tracks_df[["name","duration_ms","popularity"]].head(5))
print()
scatter_plot = sns.scatterplot(data = tracks_df, x = "popularity", y = "duration_ms")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")
fig.show()
#No existe relacion entre la popularidad y la duracion de las canciones para el artista THE MARS VOLTA