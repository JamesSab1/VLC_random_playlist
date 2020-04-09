import glob
import os
import random
import sys
import time
import vlc


def create_playlist():
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

    return playlist


def search_playlist(playlist):
    query = raw_input("Search word: ")# add multiple search by splitting
    playlist = [x for x in playlist if query in os.path.basename(x)]
    return playlist


def create_playlist_length(playlist):
    total_songs = len(playlist)
    playlist_length = raw_input("How many songs do you want to play? Enter for all ")
    if playlist_length != '':
        while not playlist_length.isdigit():
            playlist_length = raw_input("Please enter an integer value: ")
        playlist_length = int(playlist_length)
        if playlist_length > total_songs:
            print "Value larger than playlist length. Will repeat songs in the playlist."
    else:
        playlist_length = total_songs
    return [playlist_length, total_songs]


def display_songs(playlist, length_list):
    if not (playlist == [] or length_list[0] == 0):
            print "Randomly playing %s song(s) from: " % length_list[0]
            for song in playlist:
                print os.path.basename(song)            
    else:
        if not length_list[0] == "": # ugly but easy, or this prints. need better than break in loops
            print "Exiting..."
            sys.exit(0)


def fewer_songs(playlist_length, playlist):
    while (playlist_length != 0 and playlist != []):
        random_song = random.choice(playlist)
        playing = set([1,2,3,4]) # to determine when a song has finished
        p = vlc.MediaPlayer(random_song)
        p.play()
        print "Currently playing: %s" % random_song
        time.sleep(0.1) # wait briefly for it to start

        while True:
            state = p.get_state()
            if state not in playing:
                break

        playlist.remove(random_song)
        playlist_length -= 1
        if (playlist_length == 0 or playlist == []):
            print "Playlist completed"



def more_songs(playlist_length, playlist):
    while (playlist_length != 0):
        random_song = random.choice(playlist)
        playing = set([1,2,3,4]) # to determine when a song has finished
        p = vlc.MediaPlayer(random_song)
        p.play()
        print "Currently playing: %s" % random_song
        time.sleep(0.1) # wait briefly for it to start

        while True:
            state = p.get_state()
            if state not in playing:
                break
        playlist_length -= 1
        if (playlist_length == 0):
            print "Playlist completed"