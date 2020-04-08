from vlc_random_funcs import fewer_songs
from vlc_random_funcs import more_songs
from vlc_random_funcs import create_playlist
from vlc_random_funcs import create_playlist_length


#creates initial list of songs
playlist = create_playlist()

#select how many songs you want to play. Returns [playlist_length, total_songs]
length_list = create_playlist_length(playlist)

#play songs
if length_list[0] > length_list[1]:
    more_songs(length_list[0], playlist)
else:
    fewer_songs(length_list[0], playlist)