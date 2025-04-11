import spotipy
import json



class Temp_name:

    # TODO DO check if valid parameters were passed
    def __init__(self, api_client, playlist_id:str, create_file=False):
        self.api_client = api_client
        self.playlist_id:str = playlist_id


        # The function 'playlist' will fetch a playlist with the given playlist id. Returns a dict
        self.playlist:dict = self.api_client.playlist(self.playlist_id)

        # Get number of songs in playlist
        self.playlist_size:int = self.playlist['tracks']['total']
        
        
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
    


# playlist_add_items(playlist_id, items, position=None)

#     Adds tracks/episodes to a playlist

#     Parameters:

#             playlist_id - the id of the playlist

#             items - a list of track/episode URIs or URLs

#             position - the position to add the tracks


    
    def add_song(self, name, artist = None):

        query = None
        
        if artist:
            query = f'track:{name.strip()} artist:{artist.strip()}'
        else:
            query = f'track:{name.strip()}'

        item_count = 1

        search_data = self.api_client.search(q=query, type='track', limit=item_count)

        song_name = None
        song_uri = None
        song_artists = []

        for item in search_data['tracks']['items']:
            song_name = item['name']
            song_uri = item['uri']
            for artist in item['artists']:
                song_artists.append(artist['name'])
            

        # check if song is correct
        print(f'Is this the song you were looking for: {song_name} by ', end='')
        
        for i in range(len(song_artists)):

            if i + 1 < len(song_artists):
                print(f'{song_artists[i]},', end='')
            else:
                print(f" and {song_artists[i]}.")

        # TODO Add user check here. See if this is the right song that they wanted

        self.api_client.playlist_add_items(self.playlist_id, [f'{song_uri}'], self.playlist_size)
        self.playlist_size += 1


    def remove_song(self):
        pass
    