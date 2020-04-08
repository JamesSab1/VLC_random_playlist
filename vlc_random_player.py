import glob
import os
import sys
from test_funcs import fewer_songs, more_songs


###create playlist
types = ('*.mp3', '*.wav', '*.flac', '*.aac')
playlist = []
songs_dir = raw_input("Please enter a directory: ")

while not os.path.exists(songs_dir):
    songs_dir = raw_input("Please enter a valid directory, or \"Q\" to quit: ")
    if (songs_dir == "q" or songs_dir == "Q"):
        print "Exiting..."
        sys.exit(0)

else:
    answer = raw_input("Include subfolders? \"Y/N\": ")
    while not (answer in ["y", "Y", "n", "N"]):
        answer = raw_input("Please respond \"Y/N\" or \"Q\" to quit: ")
        if answer == "q" or answer == "Q":
            print "Exiting..."
            sys.exit(0)
    # plays all in subfolders
    if (answer == "Y" or answer == "y"):
        for songs_dir, subdirs, files in os.walk(songs_dir):
            for files in types:
                playlist.extend(glob.glob("%s/%s" % (songs_dir, files)))
    # if you don't want to play subfolders
    if (answer == "N" or answer == "n"):
        for files in types:
            playlist.extend(glob.glob("%s/%s" % (songs_dir, files)))
   

###select how many songs you want to play?
playlist_length = ""
if len(playlist) > 0:
    total_songs = len(playlist)
    playlist_length = raw_input("How many songs do you want to play? Enter for all ")
    if playlist_length != '':
        while not playlist_length.isdigit():
            playlist_length = raw_input("Please enter an integer value: ")
        playlist_length = int(playlist_length)
        if playlist_length > total_songs:
            print "Value larger than playlist length. Will play full playlist."
    else:
        playlist_length = total_songs


if not (playlist == [] or playlist_length == 0):
    print "Randomly playing:\n"
    for song in playlist:
        print song
else:
    if not playlist_length == "": # ugly but easy, or this prints. need better than break in loops
        print "Exiting..."
        sys.exit(0)


###play song
if playlist_length > total_songs:
    print"more"
    more_songs(playlist_length, playlist)
else:
    print "less"
    fewer_songs(playlist_length, playlist)

###todo move out other code into functions