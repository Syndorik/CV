import os
import wave
import numpy as np

os.chdir("C:/Prog tipe")

def wave2array(nchan,largech,data): #nchan = 1 (mono) 2 (stéréo) largech nb d'octet sur lequel un echantillon est codé, data retourne un tableau  où chaque élément est 1 octet de donnée(hexadecimal). Sachant qu'il y largech octet pour une donné et si on est en sétéréo il y a 2 echantillon pour un seul et même echantillongage ( gauche et droite) la formule de nb echantillon est bien le quotient de la div euclidienne de len(data) par largech*nchan
    nbechantillon, reste = divmod(len(data),largech*nchan)
    if reste>0:
        raise ValueError("la longueur du tableau n'est pas un multiple de largech* nchan") #Si reste positif, certains echantillon ne sont pas normalisé, ils sont pas codés sur le même nombre d'octet ce qui est anormal
    if largech > 4:
        raise ValueError("Une donnée d'un fichier wav décompréssé est codé sur 24 bits max")
    if largech ==3:
        a = np.array([[[0]*4]*nchan]*nbechantillon)
        datatransfo=np.fromstring(data,dtype=uint8) #on passe de la base hexadecimal à la base 10, ce n'est plus une chaine de caractère mais des entiers compris entre 0 et 255 car 1 octet = 8 bits = 2**8-1 nombres positif, chaque octet est transformé
        a[:,:,:largech]=datatransfo.reshape(-1,nchan,largech) #on suppose la stéréo on réorganise le tableau de tel sorte que pour chaque échantillon on ait les 3 octets qui codent la gauche et les 3 octets qui codent la droite
        a[:,:,largech:]=(a[:,:,largech-1:largech]>>7)*255
        result=a.view('<i4').reshape(a.shape[:-1]) #On obtient les data en base 10 entre 0 et 255
    else:
        dt_char = 'u' if largech == 1 else 'i' #Si c'est codé sur 1 octet les entiers sont signés (peuvent être negatif) si c'est codé sur 2 octets les entiers ne sont pas signés d'ou le u
        a=np.fromstring(data,dtype='<%s%d'%(dt_char,largech))
        result = a.reshape(-1, nchan)
    return(result)

def readwav(file):
    # Récupérer les données du fichier wav
    wav = wave.open(file)
    freqech= wav.getframerate()
    nchan = wav.getnchannels()
    largech=wav.getsampwidth()
    nbechantillon=wav.getnframes()
    data= wav.readframes(nbechantillon) #on prend toutes les données
    wav.close
    array = wave2array(nchan,largech,data)
    return ( freqech,largech,array)


    
        
    