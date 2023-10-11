import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import json
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import math

delete = 0
ancien_tete =0
ancien_epaule = 0

ancien_tete2 =0
ancien_epaule2 = 0

ancien_tete3 =0
ancien_epaule3 = 0
debug = []

for t in range(1,8255):
    #try:

        Write.Print(f'Figure Numero {t}', Colors.pink, interval=0.000)
        print('')
        dossier = "/home/mat/Bureau/dupdup/"
        nom_fichier = f"{t}.json"
        chemin_fichier = dossier + nom_fichier
        with open(chemin_fichier, 'r') as fichiers:
            data = json.load(fichiers)

        df = pd.DataFrame(data)
        df = df.reset_index(drop=True)
        #df = pd.DataFrame(data['results'])

        #with open(chemin_fichier, 'w') as fichier:
        #json.dump(data, fichier)
        local_max = argrelextrema(df['c'].values, np.greater, order=1, mode='clip')[0]
        local_min = argrelextrema(df['c'].values, np.less, order=1, mode='clip')[0]
        highs = df.iloc[local_max, :]
        lows = df.iloc[local_min, :]

        A = float(highs['c'].iloc[0])
        B = float(lows['c'].iloc[0])
        C = float(highs['c'].iloc[1])
        D = float(lows['c'].iloc[1])
        E = float(highs['c'].iloc[2])
        F = float(lows['c'].iloc[2])
        G = float(highs['c'].iloc[3])

        for t2 in range(1, 8255):
            # try:

            Write.Print(f'Figure Numero {t2}', Colors.pink, interval=0.000)
            print('')
            dossier2 = "/home/mat/Bureau/dupdup/"
            nom_fichier2 = f"{t2}.json"
            chemin_fichier2 = dossier2 + nom_fichier2
            with open(chemin_fichier2, 'r') as fichiers2:
                data2 = json.load(fichiers2)

            df2 = pd.DataFrame(data2)
            d2f = df2.reset_index(drop=True)
            # df = pd.DataFrame(data['results'])

            # with open(chemin_fichier, 'w') as fichier:
            # json.dump(data, fichier)
            local_max2 = argrelextrema(df2['c'].values, np.greater, order=1, mode='clip')[0]
            local_min2 = argrelextrema(df2['c'].values, np.less, order=1, mode='clip')[0]
            highs2 = df2.iloc[local_max2, :]
            lows2 = df2.iloc[local_min2, :]

            A2 = float(highs2['c'].iloc[0])
            B2 = float(lows2['c'].iloc[0])
            C2 = float(highs2['c'].iloc[1])
            D2 = float(lows2['c'].iloc[1])
            E2 = float(highs2['c'].iloc[2])
            F2 = float(lows2['c'].iloc[2])
            G2 = float(highs2['c'].iloc[3])


            if t2 != t:
                if D == D2 or F == F2:
                    debug.append(t)


print(delete)
print(debug)

