

import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import statistics
import math
import webbrowser
from operator import itemgetter
from scipy import stats
import time

#SYMBOLS ETORO/YFINANCE

#actions - energy minerals ; 
Sm = ["CVX", "XOM", "BTU", "AMR", "CNR", "PBR", "TTE.PA", "ENI.MI", "REP.MC", "RIGD.IL", "PSX", "SHEL", "VLO", 
"MPC", "COP", "HES", "PBF", "DINO", "DVN", "IEP", "EOG", "APA", "DK", "MUR", "CLMT", "BP.L", "TLW.L", "HBR.L", 
"DEC.L", "ENOG.L", "SHEL.L", "EXE", "VRN", "VET", "DNO.OL", "NESTE.HE", "IMO", "0386.HK", "0883.HK", 
"1088.HK", "1171.HK", "1898.HK", "0857.HK", "HESM", "NOG.L", "CNE.L", "VTS", "ALD.AX", "NHC.AX", "VEA.AX",
"BPT.AX", "CRN.AX", "MAU.PA", "ES.PA", "CVI", "SU", "PBR-A", "OXY", "FANG", "CTRA", "OVV", "AKRBP.OL", "EQNR.OL", "MTDR",
"SM", "CNX", "PR", "AR", "CNQ", "CRK", "CVE", "EC", "EQNR", "EQT", "CIVI", "CRC", "NOG", "YPF", "PARR", "HCC", "GPOR", 
"VIST", "NEXT", "CLB", "VNOM", "CRGY", "HPK", "METC", "HNRG", "KLXE", "GRNT", "REPX", "GPRK", "EGY", "AMPY", "EPM", "REI", 
"SMR.AX", "YAL.AX", "GFR", "METCB", "HE1.L", "GKP.L", "PANR.L", "ENQ.L", "SOU.L", "EME.L", "AET.L", "KIST.L", "CHAR.L", 
"GENL.L", "SEPL.L", "AXL.L", "RKH.L", "ORCP.L", "ECO.L", "FOG.L", "PXEN.L", "PHAR.L", "STAR.L", "BOR.L", "UJO.L",  
"ENW.L", "DR0.DE", "GALP.LS", "VAR.OL", "DOFG.OL", "BNOR.OL", "PEN.OL", "OKEA.OL", "REACH.OL", "BWO.OL", "QEC.OL", "IOX.OL", 
"PNOR.OL", "ALNG.OL", "SBX.OL", "HUNT.OL", "PSE.OL", "EC.PA"]



# actions - non energy minerals ;
Se = ["AA", "TX", "VALE", "CX", "LAR", "TKA.DE", "HEI.DE", "MTS.MC", "BZU.MI", "TEN.MI", "HOLN.SW", 
"TTST.L", "FCX", "NUE", "X", "RS", "STLD", "NEM", "IBST.L", "FXPO.L", "PDL.L", "RHIM.L", "KNF", "APAM.MC", "HH.CO", 
"PRU.AX", "CIA.AX", "CEM.MI", "KCO.DE", "ST5.DE", "BHP", "RIO", "VMC", "MLM", 
"VK.PA", "ACX.MC", "OUT1V.HE", "FLS.CO", "ROCK-B.CO", "UMI.BR", "NK.PA", "LPX", "GGB", "TREX", "SCCO", "PAAS",
"SSRM", "AEM", "AG", "AGI", "AU", "CCJ", "CDE", "0I0H.L", "EGO", "EXK", "FNV", "FSM", "GFI", "HMY", "KGC", "MT", "SBSW",
"TECK", "WPM", "BTG", "MAG", "BHP.AX", "FMG.AX", "RIO.AX", "PLS.AX", "MIN.AX", "LYC.AX", "S32.AX",
"JHX.AX", "NST.AX", "IGO.AX", "EVN.AX", "LTR.AX", "ILU.AX", "VUL.AX", "CXO.AX", "SFR.AX", "CHN.AX",
"SGM.AX", "RRL.AX", "NIC.AX", "PDN.AX", "LKE.AX", "GOR.AX", "BGL.AX", "DEG.AX", "SYR.AX", 
"FBU.AX", "CMM.AX", "WAF.AX", "JELD", "KALU", "RDUS", "LEU", "USLM", "NWPX", "ATLX", "IPX", "JHX", "LZM",
"DRD", "NEXA", "LOMA", "LXFR", "CMCL", "TG", "CTGO", "RMS.AX", "GMD.AX", "WGX.AX", "IAG", "EMR.AX", "NG",
"BOE.AX", "SAND", "EQX", "OR", "TMC", "GROY", "BMN.AX", "DVP.AX", "ABAT", "WA1.AX", "TFPM", "KAP.L",
"SRC.L", "KEFI.L", "GGP.L", "CAML.L", "KP2.L", "ALMOU.PA", "ALCOG.PA"]




Symboles = Sm+Se

Stest = ["SHEL.L", "OXY", "CVX", "BP.L", "ENI.MI", "EQT", "XOM", "TTE.PA", "TECK", "AKRBP.OL",
"CRK", "VET", "NESTE.HE", "DVN", "CNQ", "CVE", "SHEL", "PBR", "FANG", "EOG", "PBR-A"]

SymbTest = ['SIE.SG']



Input = Symboles
Tseq = 15
Selection = ['']*100 #100 pris arbitrairement pour avoir de la marge (et eviter les plantages) 
H = 0 #compteur de remplissage du tableau final 


# T1/2 ========================

for Symb in Input:
    data = yf.Ticker(Symb)
    df = round(data.history(period="1mo"), 5)
    if df.empty:
        print(Symb, " has no data")
        pass
    else:
        #print(df)
        T = len(df.index)
        Tdemi = math.floor(len(df.index)*1/2)
        #T = Tdemi
        seq = np.zeros(Tseq)
        DataNorm = np.zeros(Tseq)
        print( Symb )
        #print( "H = ", H)

    #=========TRAITEMENT===========

        for k in range(Tseq):
            seq[k] = df.iloc[k+(T-15), 3]   #Tableaux des valeurs du Symbole S à la fermeture      
            #[*, k] ; k=0 ; ouverture, k=1 ; au plus haut, k=2 ; au plus bas, k=3 ; fermeture 
            # * = 0 : premier jour du cycle, * = Tmax ; dernier jour (date actuelle)

        
        # Normalisation entre 0 et 1
        seq = (seq - np.min(seq)) / (np.max(seq) - np.min(seq) + 1e-6)  # Éviter division par zéro

        diff_seq = np.diff(seq, prepend=seq[0])  # Différences successives
        mean_diff = np.mean(diff_seq)  # Moyenne des différences
        max_min_ratio = (np.max(seq) - np.min(seq)) / (max(np.abs(np.min(seq)), 1e-3))  # Évite les explosions
        

        #D = max(seq) - min(seq)  
        Moyenne = statistics.mean(seq)    #Calcul de la moyenne
        #print(seq[Tseq-1], seq[0])

    #===========NORMALISATION==========

        #for k in range(Tseq):

        #    DataNorm[k] = round((seq[k] - min(seq))/D, 4)
        #print(H)


        Dif = round((seq[Tseq-1] - seq[0]) , 3) #Calcul du Delta initial/final, et choix de conserver la valeur ou non. seq[0] = derniere fermeture de cours
        print(Dif)
        if Dif < 0.05:
            #print(Symb, " non croissante globalement")
            pass
        else : 
            # Dif OK
            #Calcul du coefficient directeur de la droite de regression

            Days = range(Tseq)
            Coeff0 = stats.linregress(Days, seq)
            #print(Coeff0)
            Coeff = round(Coeff0[0]*10/Moyenne, 3) #coefficient directeur de la droite #====== 20 arbitraire =====
            Disp = round(Coeff0[2], 3) #coefficient de dspersion des points de la droite. =1 si alignement des points, = 0 si aucun alignement/pente definie.
            print(Coeff, Disp)
            if (Coeff < 0 or Disp < 0.6): 
                #print(Symb, " dispersion trop importante")
                pass
            else :       
                print("Coeff OK")
                T75pct = math.floor(Tseq*3/4) # pour les 25 derneirs % (mais 1/8 car)
                Dif75pct = round((seq[Tseq-1] - seq[T75pct])/Moyenne , 3)     #Calcul de la difference des cours à la fermeture dans la fin de période (derniers 25% du temps)


                if Dif75pct < 0:
                    #print(Symb, " non croissante récement")
                    pass
                else :
                    Sconf = round(Dif+Coeff+Disp/10+5*Dif75pct, 3)    # somme pour choix final            
                    Selection[H] = [Symb, " --  Coeffcient directeur : " , Coeff, " - D initial-final : " , Dif, " - D75pct : " , Dif75pct, "Dispersion : ", Disp,  " - somme de confiance ; ", Sconf]
                    #print(Selection)
                    #print(H)
                    H = H+1





#=========SORTIE===========

SelectionTab = ['']*H #Tableau final de stockage de valeur selectionnees
for i in range(H):
    SelectionTab[i] = Selection[i]


SelectionTab.sort(key=lambda x: x[10], reverse = True)

for i in range(H):
    print(SelectionTab[i])

