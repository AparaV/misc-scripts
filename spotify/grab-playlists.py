from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import csv
import sys

# Load Credentials
with open('api.json') as data_file:
    api_keys = json.load(data_file)

# Setup authentication
credentials = SpotifyClientCredentials(client_id=api_keys["CLIENT_ID"], client_secret=api_keys["CLIENT_SECRET"])
sp = spotipy.Spotify(client_credentials_manager=credentials)

# Get user name and playlist
try:
    uri = sys.argv[1]
    pass
except IndexError:
    raise ValueError("ERROR: Please provide playlist uri")
    pass

username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

playlist = sp.user_playlist(username, playlist_id)

# Open csv file
with open("tracks.csv", "wb") as csvfile:

    # setup headers
    fields = ["Title", "Artists", "Album"]
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    # add track
    for track in playlist["tracks"]["items"]:

        # get track info
        name = track["track"]["name"]
        artists = ""
        for i in range(len(track["track"]["artists"]) - 1):
            artists = artists + track["track"]["artists"][i]["name"] + ","
        artists = artists + track["track"]["artists"][len(track["track"]["artists"]) - 1]["name"]
        album = track["track"]["album"]["name"]

        # write to file
        try:
            writer.writerow({"Title": name, "Artists": artists, "Album": album})
            pass
        except UnicodeEncodeError:
            writer.writerow({"Title": name, "Artists": artists, "Album": "Album cannot be decoded"})
            pass
