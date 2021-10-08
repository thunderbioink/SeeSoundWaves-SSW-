from welcome import print_welcome

from emma import print_emma
from josh import print_josh
from ana import print_ana
from david import printDavid
import time

print_welcome()

print_emma()
print_josh()
print_ana()
printDavid()


import wave, struct

wave_file = wave.open('..\ssw_program\wav_files\Blue_UnmasteredWAV.wav', 'r')

length = wave_file.getnframes()
for i in range(0, length):
    wave_data= wave_file.readframes(48000)
    data = struct.unpack('<48000h', wave_data) 
    
    print(int(data[0]))



import soundfile as sf

data, samplerate = sf.read('../wav_files/Blue_UnmasteredWAV.wav')
from scikits import audiolab
from scipy.io import wavfile
from sys import argv
for filepath in argv[1:]:
    x, fs, nb_bits = audiolab.wavread(filepath)
    print('Reading with scikits.audiolab.wavread:', x)
    fs, x = wavfile.read(filepath)
    print('Reading with scipy.io.wavfile.read:', x)
