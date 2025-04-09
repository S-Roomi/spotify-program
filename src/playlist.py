import spotipy
import json



class Playlist:

    def __init__(self, api_client, playlist_id):
        self.api_client = api_client
        self.playlist_id = playlist_id

    def getSongs(self, size):
        #see information in json file
        # with open("spotifyInfo.json", "w") as outfile: 
        #     json.dump(user_playlist["items"], outfile, indent=1)

        playlist_offset = 0
        keepIterate = True

        list_of_songs = []

        while (keepIterate):
            user_playlist = (self.api_client).playlist_items(playlist_id=id, offset=playlist_offset)
            for index, elem in enumerate(user_playlist["items"]):
                # “uri”:”4iV5W9uYEdYUVa79Axb7Rh”, “positions”:[2] 
                list_of_songs.append((elem["track"]["name"], {"uri":elem["track"]["uri"],"positions":[index+playlist_offset]}))

            
            if (playlist_offset + 100 > size):
                keepIterate = False
            else:
                playlist_offset += 100
            
        return list_of_songs

    def removeDuplicate(self, songs,playlist_id):
        # Data
        playlist_id = playlist_id # The ID of the playlist containing the tracks to be deleted

        track_ids = []
        seen = []

        for i in songs:
            if (i[0] in seen):
                track_ids.append(i[1])
            else:
                seen.append(i[0])

        # Call the track deletion function
        if (track_ids):
            sp.playlist_remove_specific_occurrences_of_items(playlist_id=playlist_id, items=track_ids)


    def addSongs(self, sp, playlist_id):
        list_of_id = []

        user_input = ""
        stop = False
        print("Enter URL of songs, type quit to stop")

        while (stop == False):
            
            user_input = input(user_input)

            if (user_input == "quit"):
                stop = True
                break
            else:
                list_of_id.append(user_input)

            user_input = ""


        if (list_of_id):
            sp.playlist_add_items(playlist_id=playlist_id, items=list_of_id)
