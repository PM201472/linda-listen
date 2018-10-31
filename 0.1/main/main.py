# This file contains the core of the linda code

## Options
# boot_mode = 1: Start Normaly
# boot_mode = 2: Add Sample Audio

# probability: 1-100 the lower the probability, the more senstive

# max_rec_time: the higher the number the more time it takes to save
# if rec goes over time, it will simply not record. (MIN 1)
boot_mode = 2
probability = 50
max_rec_time = 1
## /

# Imports Dependencies
from speech import *
import numpy as np
import sounddevice as sd
import os
from time import sleep
# /

print ("Starting Linda...")

## Some defined functions
# record(length, samplerate, channels)
# sample_rec(length, samplerate, channels)
# sample_check(command)
# /

# Normal Boot
if boot_mode == 1:
    print ("Starting Linda Normaly..")
    recording = record(1, 44100, 2)
    print (recording)
# /

# Add Audio Sample
if boot_mode == 2:
    print ("Starting Linda in Sample Creation Mode..")
    print ("\nSelect the Command:")
    print ("1) linda_listen")
    print ("2) say_hi")
    print ("3) what_time_is_it")
    print ("4) who_am_i")
    done = False

    while done == False:
        response = input()
        if response == '1':

            print ('-------------------')
            done = True
            last = sample_check('linda_listen')
            last_file_path = 'commands/linda_listen/' + str(last)
            recording = open(last_file_path, 'a')
            recording.write(str(sample_rec(max_rec_time, 44100, 2)))
            recording.close()
            print ('Done!')

        elif response == '2':

            print ('-------------------')
            done = True
            last = sample_check('say_hi')
            last_file_path = 'commands/say_hi/' + str(last)
            recording = open(last_file_path, 'a')
            recording.write(str(sample_rec(max_rec_time, 44100, 2)))
            recording.close()
            print ('Done!')

        elif response == '3':

            print ('-------------------')
            done = True
            last = sample_check('what_time_is_it')
            last_file_path = 'commands/what_time_is_it/' + str(last)
            recording = open(last_file_path, 'a')
            recording.write(str(sample_rec(max_rec_time, 44100, 2)))
            recording.close()
            print ('Done!')

        elif response == '4':

            print ('-------------------')
            done = True
            last = sample_check('who_am_I')
            last_file_path = 'commands/who_am_I/' + str(last)
            recording = open(last_file_path, 'a')
            recording.write(str(sample_rec(max_rec_time, 44100, 2)))
            recording.close()
            print ('Done!')

        else:

            done = False
            print ('Error, Try Again:')
# /
