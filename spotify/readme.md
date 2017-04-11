# Scripts for Spotify

## Requirements
To run these, you need `spotipy`

To install
```
$ pip install -r requirements.txt
```
Additional instructions are present inside each script if applicable.
To use these scripts, you will need to put your `CLIENT_ID` and `CLIENT_SECRET` in `api.json file` as a `JSON` file with the said keys.

## Files

### 1. [Grab tracks info from playlists](grab-playlists.py)

Use this as: (the playlist URI as a command line argument)
```
$ python grab-playlists.py spotify:user:XXXXXX:playlist:XXXXXXXXXXXXXXXX
```
The tracks with Title, Artist(s), and Album will be saved in `tracks.csv` in `.csv` format.
