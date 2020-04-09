import sys

from vlc_random_funcs import fewer_songs
from vlc_random_funcs import more_songs
from vlc_random_funcs import create_playlist
from vlc_random_funcs import create_playlist_length
from vlc_random_funcs import display_songs
from vlc_random_funcs import search_playlist


#creates initial list of songs
playlist = create_playlist()

#optional search - shoud this bit be in the function, or should bits be moved
#from other functions?
answer = raw_input("Apply a filter \"Y/N\": ")
while answer not in ["y", "Y", "n", "N"]:
    answer = raw_input("Please respond \"Y/N\" or \"Q\" to quit: ")
    if answer == "q" or answer == "Q":
        print "Exiting..."
        sys.exit(0)
if (answer == "Y" or answer == "y"):
    playlist = search_playlist(playlist)
    if playlist == []:
        print "Playlist empty\nExiting..."
        sys.exit()

#select how many songs you want to play. Returns [playlist_length, total_songs]
length_list = create_playlist_length(playlist)

#display songs
display_songs(playlist, length_list)

#play songs
if length_list[0] > length_list[1]:
    more_songs(length_list[0], playlist)
else:
    fewer_songs(length_list[0], playlist)