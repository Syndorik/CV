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

Gson2 = (read("Essai2.wav")[1])
rate2=(read("Essai2.wav")[0])

    
def downsample(signal,freqech): #Sous echantilloner de 44.1Khz à 11.025 revient à prendre 1 élément sur 4
    Newdata=[]
    if not os. path.exists(signal):
        print("Pas de signal trouvé")
        return False   
    data=read(signal)[1]
    rate=read(signal)[0]
    for k in range(0,len(data),int(rate/freqech)):
        Newdata+=[data[k]]
    return(Newdata)

def Time(signal):
    data=read(signal)[1]/(2**15)
    rate=read(signal)[0]
    print(rate)
    print(len(data))
    return(len(data)*1/rate)

Ssechan=downsample("Essai Audacity.wav",11025)

#Creation d'un fichier wav
def tab2wav(Fichier,Sigssech,frecec):
    oui=np.array(Sigssech)
    write(Fichier,frecec,oui)
#tab2wav("lalala.wav",Ssechan,11025)

Gson3=(read("lalala.wav")[1]/(2**15))




