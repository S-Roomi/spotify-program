import spotipy
import json



class Temp_name:

    # TODO DO check if valid parameters were passed
    def __init__(self, api_client, playlist_id:str, create_file=False):
        self.api_client = api_client
        self.playlist_id:str = playlist_id


        # The function 'playlist' will fetch a playlist with the given playlist id. Returns a dict
        self.playlist:dict = self.api_client.playlist(self.playlist_id)

        # Get number of tracks in playlist
        self.playlist_size:int = self.playlist['tracks']['total']
        
        
        if create_file == True:
            with open('playlist_data.json', 'w') as json_file:
                json.dump(self.playlist, json_file)
        

    
    def get_playlist(self):
        return self.playlist

    def get_tracks(self):
        """
        Returns a list of track names that were found in the given playlist
        """
        track_list = []

        for item in self.playlist['tracks']['items']:
            track_list.append(item['track']['name'])
        
        return track_list
        
        
    def find_track(self, track_name):
        """
        Takes in a track name and searches for that track. Uses playlist from given playlist_id.
        """

        if not track_name:
            print("Need valid track name.")
            return None
        
        index = 0

        for item in self.playlist['tracks']['items']:
            if item['track']['name'] == track_name:
                return [item['track'], index]
            index += 1
        
        return None
    


# playlist_add_items(playlist_id, items, position=None)

#     Adds tracks/episodes to a playlist

#     Parameters:

#             playlist_id - the id of the playlist

#             items - a list of track/episode URIs or URLs

#             position - the position to add the tracks


    
    def add_track(self, name, artist = None):

        query = None
        
        if artist:
            query = f'track:{name.strip()} artist:{artist.strip()}'
        else:
            query = f'track:{name.strip()}'

        item_count = 1

        search_data = self.api_client.search(q=query, type='track', limit=item_count)

        track_name = None
        track_uri = None
        track_artists = []

        for item in search_data['tracks']['items']:
            track_name = item['name']
            track_uri = item['uri']
            for artist in item['artists']:
                track_artists.append(artist['name'])
            

        # check if track is correct
        print(f'Is this the track you were looking for: {track_name} by ', end='')
        [print(x) for x in track_artists] # not the best way to print a list but saw it online and though it looked cool

        # TODO Add user check here. See if this is the right track that they wanted

        self.api_client.playlist_add_items(self.playlist_id, [f'{track_uri}'], self.playlist_size)
        self.playlist_size += 1


    def remove_track(self, track_name:str, first_occurrence=False, all_occurrence=False):
        track = self.find_track(track_name)
        
        if track == None:
            print("Track does not exist")
            return None

        if all_occurrence == True:
            self.api_client.playlist_remove_all_occurrences_of_items(self.playlist_id, [f'{track[0]['uri']}'])
        elif first_occurrence == True: # TODO always removes all occurrences.
            # Not sure if I can remove specific indexes. Documentation of playlist_remove_specific_occurrences_of_items mentions all items. 
            item = [{'uri': track[0]['uri'], 'positions':[track[1]]}]
            print(track[1])
            self.api_client.playlist_remove_specific_occurrences_of_items(self.playlist_id, item)
        else:
            print("Please define if you wish to remove the first occurrence of a song or all occurrences of a song")
            return None
    