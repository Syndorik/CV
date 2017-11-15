import os
import algo.fingerprint as fingerprint
import algo.wavv as wavv
import sqlite3 as sql
import numpy as np
import time
base = sql.connect("mabase.db")
cursor=base.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS F(
    id varchar
)
""")
base.commit()

def empreinte(file):
    ech = fingerprint.stereo2mono(file)
    return(fingerprint.fingerprint(ech))

def match(file):
    matchs=[]
    matchs.extend(empreinte(file))
    matchs=np.array(matchs)
    matchs=matchs[:,0]
    return(matchs)

def empreinte_enregistre_base(file,Nom):
    to = time.clock()
    matchs=match(file)
    np.save("%s"%Nom,matchs)
    cursor.execute("""INSERT INTO F(id) values ('%s')""" %(Nom))
    base.commit()
    return(to-time.clock())

def compare(m,filedb):
    n=len(m)
    fdb=np.load("%s.npy"%filedb)
    c=(set(m).intersection(fdb))
    return(len(c)/n)

def recognize(file): #Très long pour certains fichier
    m=match(file)
    cursor.execute("""SELECT id FROM F""")
    user = cursor.fetchall()
    pourcent=0
    sol=0
    for k in range(len(user)):
        p=pourcent
        pour=compare(m,user[k])
        pourcent=max(pour,pourcent)
        if p != pourcent:
            sol=k
    return(user[sol],pourcent)
        
        
        
        
        
        
    



