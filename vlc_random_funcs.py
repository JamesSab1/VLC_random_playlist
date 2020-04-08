import random
import vlc
import time


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