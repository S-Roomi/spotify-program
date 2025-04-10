import spotipy
from spotipy.oauth2 import SpotifyOAuth
from playlist import Temp_name

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    playlist_id = '0LVCb93GAzod0uYoMbjpMk'

    scope = "playlist-modify-public"

    #Authorization
    api_client = spotipy.Spotify(auth_manager = SpotifyOAuth(scope=scope))

    # create Playlist object
    user = Temp_name(api_client, playlist_id)
    user.add_song(name='Love', artist='Kendrick')




