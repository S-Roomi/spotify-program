import spotipy
from spotipy.oauth2 import SpotifyOAuth
from playlist import Playlist

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    username = "Lil Na"
    playlist_id = '0LVCb93GAzod0uYoMbjpMk'
    playlist_size = 0

    scope = "playlist-modify-public"

    #Authorization
    api_client = spotipy.Spotify(auth_manager = SpotifyOAuth(scope=scope))

    # create Playlist object
    user_playlist = Playlist(api_client, playlist_id)
    




