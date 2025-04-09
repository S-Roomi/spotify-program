import spotipy
import json



class Temp_name:

    # TODO DO check if valid parameters were passed
    def __init__(self, api_client, playlist_id, create_file=False):
        self.api_client = api_client
        self.playlist_id = playlist_id


        # The function 'playlist' will fetch a playlist with the given playlist id. Returns a dict
        self.playlist = self.api_client.playlist(self.playlist_id)

        # Get number of songs in playlist
        self.playlist_size = self.playlist['tracks']['total']
        
        
        if create_file == True:
            with open('playlist_data.json', 'w') as json_file:
                json.dump(self.playlist, json_file)
        

    
    def get_playlist(self):
        return self.playlist

    def get_songs(self):
        """
        Returns a list of song names that were found in the given playlist
        """
        song_list = []

        for item in self.playlist['tracks']['items']:
            song_list.append(item['track']['name'])
        
        return song_list
        
        
    def find_song(self, song_name, song_list=None):
        """
        Takes in a song name and searches for that song. Uses playlist from given playlist_id.
        If a song list was passed as a parameter, iterate over the song list
        """

        if not song_name:
            print("Need valid song name.")
            return None
    
        for item in self.playlist['tracks']['items']:
            if item['track']['name'] == song_name:
                return item['track']
        
        return None
    
    def add_song(self):
        pass

    def remove_song(self):
        pass
    