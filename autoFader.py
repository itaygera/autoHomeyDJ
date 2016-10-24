# insert a path of a desired directory
# plays all the mp3 in the directory
# preforming an overlap between each two songs
# decrease the volume of the first song in the overlap
import os
from random import shuffle
import vlc
from time import sleep
from mutagen.mp3 import MP3

directory = "" # here goes your music directory absolute path
overlapTime = 20; # the overlap time between two songs
decreaseTo = 85; # the volume that the song will be decreased to during the overlap

songsNames = os.listdir(directory) # get all the files from the directory
shuffle(songsNames) # shuffle their order - can be removed, if wanted
print(songsNames)
for filename in songsNames:
    if filename.endswith(".mp3"): # possible extend: or filename.endswith(".mp4") # right now only supports mp3
        absolotePath = os.path.join(directory, filename)
        print("started: " + filename)
        p = vlc.MediaPlayer(absolotePath)
        audio = MP3(absolotePath)
        lengthInSeconds = audio.info.length # get the length of the song in seconds
        # print(vlc.libvlc_media_player_get_length(p))
        # lengthInMs = p.get_length()
        # lengthInMs = vlc.libvlc_media_get_duration(p)
        # lengthInSeconds = lengthInMs / 1000
        vlc.libvlc_audio_set_volume(p, 100)
        p.play()
        print(vlc.libvlc_audio_get_volume(p))
        sleep(max(lengthInSeconds - overlapTime,0))
        vlc.libvlc_audio_set_volume(p, decreaseTo)
        print(vlc.libvlc_audio_get_volume(p))
        print("finished: " + filename)
sleep(overlapTime)
print("finished all playlist!")