# This is the speech recognition file
boot_mode = 1
probability = 30
max_rec_time = 5
sample_rate = 44100
channels = 2

# Imports Dependencies
import numpy as np
import sounddevice as sd
import os
from time import sleep
from timeit import default_timer as timer
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
    start = timer()
    input()
    print ('Stoping...')
    sd.stop()
    stop = timer()
    time = stop - start
    print ('Saving..')
    samples = round(time * samplerate)
    sound_input = sound_input.tolist()
    sound_input = sound_input[:samples]
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

# This def is used to preload all the audio sample files.
def preload_audio(command, channels):
    samples = sample_check(command) - 1
    path = 'commands/' + command + '/'
    data = []
    for i in range(samples):
        file_number = i + 1
        file = open(path + str(file_number), 'r+')
        line = file.readline()
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.replace(',', '')
        list = []
        temp = []
        times = 0
        for u in line.split():
            times = times + 1
            list.append(u)
            if times == channels:
                temp.append(list)
                list = []
                times = 0
        file.close()
        data.append(temp)
    audio_data = data
    return audio_data
#/

linda_listen_preload = preload_audio('linda_listen', channels)
say_hi_preload = preload_audio('say_hi', channels)
what_time_is_it_preload = preload_audio('what_time_is_it', channels)
who_am_I = preload_audio('who_am_I', channels)

# This where the audio recognition takes place
def find_rate(command, sample):
    rate = len(command[sample-1])
    rate = 100 / rate

def probability(audio, command, sample):
    real_probability = 0
    data = command[sample-1]
    for i in range(find_rate(command, 1)):
        print (i)
        sleep(1)
    return (real_probability)

def check_audio(audio):
    probability(audio, linda_listen_preload, 1)
#/
