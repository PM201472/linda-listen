# This is the speech recognition file

# Imports Dependencies
import numpy as np
import sounddevice as sd
import os
from time import sleep
# /

# This def records the sound and puts it into a numpy array
def record(length, samplerate, channels):
    np.set_printoptions(threshold=np.nan)
    sd.default.samplerate = samplerate
    sd.default.channels = channels
    sound_input = sd.rec(int(length)*int(samplerate))
    sleep(length)
    return (sound_input)
# /

# This def is used to make audio samples
def sample_rec(length, samplerate, channels):
    np.set_printoptions(threshold=np.nan)
    sd.default.samplerate = samplerate
    sd.default.channels = channels
    print ('Press Enter to Start/Stop Recording')
    input()
    print ('Starting...')
    sound_input = sd.rec(int(length)*int(samplerate))
    input()
    print ('Stoping...')
    sd.stop()
    print ('Saving..')
    sound_input = str(sound_input)
    sound_input = sound_input.replace('0.00000000e+00  0.00000000e+00', '')
    sound_input = sound_input.replace(' [ ]\n', '')
    sound_input = sound_input.replace('\n [ ]', '')
    return (sound_input)
#/

# This def is used to check for old audio samples.
# It does this to keep from over writing previous saves
def sample_check(command):
    command_path = 'commands/' + command + '/'

    last_found = False
    loops = 0
    while last_found == False:
        loops = loops + 1
        full_path = (str(command_path) + str(loops))
        check = os.path.isfile(full_path)
        if check == False:
            last_found = False
            return (loops)
# /
