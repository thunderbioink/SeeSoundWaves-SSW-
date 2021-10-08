# 1st step, import wave

import wave
import numpy as np 
# convert soudnwave from bytes to integers



    
# 2nd step, import audio file as wave object 

blue_unmastered = wave.open("C:/Users/Alma/Documents/SSW/SeeSoundWaves-SSW-/ssw_program/playsound/Blue_UnmasteredWAV.wav", "r")

# 3rd step, convert my object to bytes

blue_unmastered_soundwave = blue_unmastered.readframes(-1)

# 4th step, view the wav file in byte form

blue_unmastered_soundwave

# 5th step
signal_gm = np.frombuffer(blue_unmastered_soundwave)    
    
















