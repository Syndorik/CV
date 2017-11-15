#import matplotlib
#matplotlib.use('Agg')
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import os
import wave
import math
import binascii

os.chdir("C:/Prog tipe")
#Gson = (read("TIPE/WAV/fichiermusicale")[1]/(2**14)) #Fichier audio
Gson = (read("Essai Audacity 11K.wav")[1]/(2**15)) #2**15 car le son est quantifié sur 16 bits et on veut amplitude de 2 (ymin/ymax)
rate=(read("Essai Audacity 11K.wav")[0])
print(rate)

Gson2 = (read("Essai Audacity.wav")[1]/(2**15))
rate2=(read("Essai Audacity.wav")[0])
print(rate2)
    