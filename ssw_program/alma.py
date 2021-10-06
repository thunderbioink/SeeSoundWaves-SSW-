# def print_alma():
#         print("Hello!This is Alma Camarillo! ")
    
#     # python hello_program
    
    


# import os
# print('current directory')
# print(os.getcwd())

# print(1*2)
# print(2**3)


# import wave, struct

# wave_file = wave.open('..\ssw_program\wav_files\Blue_UnmasteredWAV.wav', 'r')

# length = wave_file.getnframes()
# for i in range(0, length):
#     wave_data= wave_file.readframes(48000)
#     data = struct.unpack('<48000h', wave_data) 
    
#     print(int(data[0]))



# import soundfile as sf

# data, samplerate = sf.read('../wav_files/Blue_UnmasteredWAV.wav')
# from scikits import audiolab
# from scipy.io import wavfile
# from sys import argv
# for filepath in argv[1:]:
#     x, fs, nb_bits = audiolab.wavread(filepath)
#     print('Reading with scikits.audiolab.wavread:', x)
#     fs, x = wavfile.read(filepath)
#     print('Reading with scipy.io.wavfile.read:', x)


""" Import Modules and packages"""



# import librosa as lr


# import matplotlib

# matplotlib.__version__
# Test if matplotlib installes after pip install. No error message. Successful


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from glob import glob
# import py audio
# import librosa as lr

# # continue here to create directory path for source files

# data_dir = '.\ssw_program\wav_files'

# audio_files = glob(data_dir + '/*.wav')

# # len(audio_files)

# audio, sfreq = lr.load(audio_files[0])
# time = np.arange(0, len(audio)) / sfreq 


# fig, ax = plt.subplots()
# ax.plot(time, audio)
# ax.set(xlabel ='Time (s)', ylabel= 'Sound Amplitude')

# plt.show()



#1st successful attempt to pull audio wave image, small EQ parameter settings, can save and manipualte WAV. Haven't made official changes to file. 



#!/usr/bin/env python3
"""Create a recording with arbitrary duration.

The soundfile module (https://PySoundFile.readthedocs.io/) has to be installed!

"""
import argparse
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args(remaining)

q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])
    if args.filename is None:
        args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
                                        suffix='.wav', dir='')

    # Make sure the file is opened before recording anything:
    with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                      channels=args.channels, subtype=args.subtype) as file:
        with sd.InputStream(samplerate=args.samplerate, device=args.device,
                            channels=args.channels, callback=callback):
            print('#' * 80)
            print('press Ctrl+C to stop the recording')
            print('#' * 80)
            while True:
                file.write(q.get())
except KeyboardInterrupt:
    print('\nRecording finished: ' + repr(args.filename))
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))





import librosa as lr


import matplotlib

matplotlib.__version__
# Test if matplotlib installes after pip install. No error message. Successful


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import py audio
import librosa as lr

# continue here to create directory path for source files

data_dir = '.\ssw_program\wav_files'

audio_files = glob(data_dir + '/*.wav')

# len(audio_files)

audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq 


fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel ='Time (s)', ylabel= 'Sound Amplitude')

plt.show()


