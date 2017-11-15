import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import (generate_binary_structure,
                                      iterate_structure, binary_erosion)
import hashlib
from scipy.io.wavfile import read
from operator import itemgetter
import algo.wavv as wavv

""" On va utiliser des fonctions de hachage pour coder l'algo d'empreinte en particulier SHA1"""
#Frequence echantillonage qui est troujours de 44100 Khz
Def_freqe=44100
#Taille de la fenêtre FFT
Def_taille_fenetre = 4096
#Ratio de Chevauchement, ex 0.5 chaque fenetre (de FFT) va empieter à moitier sur la suivante et à moitié sur la précédente, plus ce ratio est grand plus la précision est grande ce qui implique qu'il y a plus d'empreinte
Def_ratio_chevauch = 0.5
#Degré avec lequel une empreinte peut être associé à ses voisins, plus c'est grand plus c'est précis.
Def_degre=15
#Amplitude minimum qui peut être considéré comme un pique
Def_Amp_min=10
#Seuil pour lesquels deux empreintes peuvent être éloignés en temps de telle sorte qu'elles puissent être associé comme empreinte, si le max est trop faible on peut avoir des pb avec degré
Min_hash_time = 0
Max_hash_time = 200
#Nombre de points autour d'un pique dans le spectrogramme pour le considérer comme un pique
Def_taille_pique = 20
#Vrai : on trie les empreintes chronologiquement pour l'algorithme
Tri_des_piques = True
#Nombre de bit à enlever pour le resultat de SHA1 plus on en enlève moins cela va peser mais plus on peut avoir de collision et de mauvaise interpretation
Reduction_hash=20
plot = True
realtimeplot = False

def fingerprint(ech, fe = Def_freqe, tfen= Def_taille_fenetre, rchev = Def_ratio_chevauch, deg= Def_degre, amp_min=Def_Amp_min): #ech = data
    """ On fait la FFT d'un canal (1 ou 2 selon mono/stéréo), on cherche les piques maximum caractéristiques et on retourne les hash correspondant, les fonctions maxloc et hashs sont celles qui permettent la génération d'empreinte pour 1 FFT"""
    #FFT
    FFT = mlab.specgram(ech, NFFT= tfen, Fs=fe, window = mlab.window_hanning,noverlap = int(tfen*rchev))
    spec2D= FFT[0] #Peridogramme = densité de puissance des fréquence sur chaque segment de temps
    #On applique le log car spec renvoie une echelle linéaire
    spec2D = 10*np.log10(spec2D)
    spec2D[spec2D == -np.inf] = 0 # à cause du log on peut avoir des - infini on remplace par des 0
    maxlocaux = maxloc(spec2D,FFT[1],FFT[2],amp_min)
    return hashs(maxlocaux,deg = deg)
    
    
    
def maxloc(arrray,Freq,Temps,plot=plot, amp_min= Def_Amp_min,taillepique= Def_taille_pique,realtimeplot=realtimeplot):
    """On va compartimenter le spectrogram, de telle sorte que dans un "rayon de taillepique" on ait que une seule valeur """
    structure = generate_binary_structure(2,1) # tableau de booléen ceux à 1 de distance du centre sont True les autres False
    voisin = iterate_structure(structure, taillepique)
    MAX = maximum_filter(arrray, footprint =voisin) #On a compartimenté le spectrogramme en "carré"
    #print(MAX)
    locmax = (MAX == arrray) #Tableau de booléen traduisant la localisation des maximum, il suffit de trouver la localisation des True
    background = (arrray == 0) #True si 0 pour l'array background
    erosion = binary_erosion(background, structure = voisin) # Les true qui sont compris dans le "carré de rayon taillepique" deviennent False
    dpique = locmax-erosion # On supprime les valeurs nulles de specgram ( car ce ne sont pas des pique d'amplitude)
    amps= arrray[dpique] #Tableau d'une seule ligne contenant les amplitudes
    y,x= np.where(dpique) #x et y tableau des indices des amplitudes
    pique= list(zip(x,y,amps))
    #Filtre des amplitudes
    n = len(amps)
    c=0
    for k in range(n):
        if amps[k]< amp_min:
            pique[k]=0
            c+=1
    for k in range(c):
        pique.remove(0)
    frequence_associe=[]
    time_associe =[]
    for k in range(len(pique)):
        frequence_associe+=[pique[k][1]]
        time_associe+=[pique[k][0]]
    
    if plot==True:
        fig,ax= plt.subplots()
        ax.imshow(arrray)
        ax.scatter(time_associe,frequence_associe)
        ax.set_xlabel("Temps")
        ax.set_ylabel("Frequence")
        ax.set_title("Spectrogramme")
        plt.gca().invert_yaxis()
        plt.show
    
    if realtimeplot:
        fig,ax= plt.subplots()
        plt.pcolor(Temps,Freq,arrray)
        n = len(time_associe)
        nt=np.zeros(n)
        p = len(frequence_associe)
        nf=np.zeros(p)
        for k in range(n):
            nt[k]=Temps[time_associe[k]]
        for k in range(p):
            nf[k]=Freq[frequence_associe[k]]
        ax.scatter(nt,nf)
        ax.set_xlabel("Temps")
        ax.set_ylabel("Frequence")
        ax.set_title("Spectrogramme")
        plt.show
    return(list(zip(frequence_associe,time_associe)))

def stereo2mono(file):
    r=wavv.readwav(file)
    frequ=r[0]
    data=r[2]
    try:
        n,p = np.shape(data)
    except(ValueError):
        p=0
    if p==2:
        for k in range(p):
            for j in range(n):
                if data[j][p-1]<0:
                    data[j][p-1]= - data[j][p-1]
                if data[j][0]<0:
                    data[j][0]=-data[j][0]
        mono=np.mean(data,axis=1)
        return(mono)
    else:
        for k in range(len(data)):
            if data[k]<0:
                data[k]=-data[k]
        return(np.array(data))
        

def hashs(pique,deg=Def_degre):
    """On utilise la structure de hachage sha1 pour coder les empreintes"""
    if Tri_des_piques:
        pique.sort(key = itemgetter(1)) #On trie selon le temps
    
    for i in range(len(pique)):
        for j in range(1,deg):
            if (i+j)< len(pique):
                freq1 = pique[i][0]
                freq2= pique[j+i][0]
                t1 = pique[i][1]
                t2 = pique[i+j][1]
                dt = t2-t1
                
                if dt>=Min_hash_time and dt<=Max_hash_time: #Valeurs à respecter pour créer une hash
                    s = "%s|%s|%s"% (str(freq1), str(freq2), str(dt))
                    h= hashlib.sha1(s.encode()) #On encode
                    yield (h.hexdigest()[:], t1) #Générateur de hash

def Compare_avec_bruit(file1,file2): #marche très bien mais que sur la même durée et si pas bcp de saturation
    ech1 = stereo2mono(file1)   #En effet si saturation amplitude trop haute et le bruit trop conséquent
    ech2 = stereo2mono(file2)
    finger1 = fingerprint(ech1)
    finger2 = fingerprint(ech2)
    f1=[]
    f2=[]
    for j in finger1:
        f1+=j
    for i in finger2:
        f2+=i
    c=(set(f1).intersection(f2))
    return(len(c)/max(len(set(f1)),len(set(f2))))

    