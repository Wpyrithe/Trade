

import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import statistics


#ETORO

#actions - energy minerals ; 
S1 = ["SHEL.L", "OXY", "CVX", "BP.L", "ENI.MI", "EQT", "XOM", "TTE.PA", "TECK", "AKRBP.OL",
"CRK", "VET", "NESTE.HE", "DVN", "CNQ", "CVE", "SHEL", "PBR", "FANG", "EOG", "PBR-A",
 "SU", "MRO", "COP", "OVV", "CPG", "NOG", "IEP", "DK", "CHRD", "REP.MC", "PXD", "BTU",
  "PBF", "CTRA", "0386.HK", "VLO", "PSX", "EQNR.OL", "AMR", "TELL", "VTS", "CPE", "VTLE",
   "MPC", "ARCH", "MTDR", "E", "EC", "SWN", "1088.HK", "WHC.AX", "WDS", "HES", "PGS.OL",
    "TLW.L", "EQNR", "MGY", "CNX", "APA", "DINO", "SM", "NFG", "CHK", "NOG.L", "CVI", "DEN",
     "0883.HK", "CIVI", "TTE", "CEIX", "WTI", "ERF", "KOS", "1898.HK", "1171.HK", "BP",
      "DNO.OL", "PR", "CRC", "MUR", "SRS.MI", "RRC", "HESM", "CNE.L", "CLMT", "IMO"]

#LOST  "PDCE"

# actions - non energy minerals ;
S2 = ["GOLD", "VALE", "FCX", "NHY.OL", "FXPO.L", "ROCK-B.CO", "NDA.DE", "MTS.MC", "BOL.ST", "NUE",
 "RIO", "3323.HK", "MAG", "RIO.L", "NEM", "BHP", "SZG.DE", "TKA.DE", "CCJ", "FNV", "PAAS", "X", "MP",
  "LPX", "SBSW", "GGB", "WPM", "MLM", "CEY.L", "KGC", "AESI", "AAL.L", "FSM", "AG", "AA", "HEI.DE",
   "2899.HK", "TX", "AEM", "BHP.L", "STLD", "SCCO", "PDL.L", "BTG", "RS", "TREX", "CX", "TEN.MI",
    "HMY", "GFI", "CLF", "0914.HK", "PKX", "AU", "TS", "CDE", "ACX.MC", "UMI.BR", "CMC", "SSRM",
     "SLCA", "AGI", "VK.PA", "HOC.L", "HL", "ANTO.L", "SID", "NK.PA", "EXK", "HOLNZ.XC", "MT",
      "CRH.L", "VMC", "KNF", "IBST.L", "0MKX.IL", "EGO", "RGLD", "APAM.AS", "ATI", "BZU.MI", "FLS.CO",
       "MSLH.L", "MHK", "RHIM.L", "NCMGF", "SUM", "EXP", "TKTT.PA"]

#LOST "ARNC"



Symb = S1+S2

#ETORO1
["SHEL.L", "OXY", "CVX", "BP.L", "ENI.MI", "EQT", "XOM", "TTE.PA", "TECK", "AKRBP.OL",
"CRK", "VET", "NESTE.HE", "DVN", "CNQ", "CVE", "SHEL", "PBR", "FANG", "EOG", "PBR-A",
 "SU", "MRO", "COP", "OVV", "CPG", "NOG", "IEP", "DK", "CHRD", "REP.MC", "PXD", "BTU",
  "PBF", "CTRA", "0386.HK", "VLO", "PSX", "EQNR.OL", "AMR", "TELL", "VTS", "CPE", "VTLE",
   "MPC", "ARCH", "MTDR", "E", "EC", "SWN", "1088.HK", "WHC.AX", "WDS", "HES", "PGS.OL",
    "TLW.L", "EQNR", "MGY", "CNX", "APA", "DINO", "SM", "NFG", "CHK", "NOG.L", "CVI", "DEN",
     "0883.HK", "CIVI", "TTE", "CEIX", "PDCE", "WTI", "ERF", "KOS", "1898.HK", "1171.HK", "BP",
      "DNO.OL", "PR", "CRC", "MUR", "SRS.MI", "RRC", "HESM", "CNE.L", "CLMT", "IMO"]





#ANCIENS TESTS
["ATNXQ", "RIDE", "TOON", "HTGMQ", "IDEX", "ENVX", "WISE.L", "FRCB", "1628.HK", "CAMP", "TBLT", "RAD", "WATT", "SOLO", "INO", "AIHS", "CCL.L", "XXII", "U", "CGC", "MARA", "WKHS", "WBA", "ADMP", "ZYNE", "CARA", "JFU", "AMRS", "HA", "LEO.DE", "HUT", "ORGN", "1966.HK", "PGS.OL", "BHG", "QFIN", "2007.HK", "TEP.L", "HICL.L", "PAT.DE", "DSHK", "COIN", "NIO", "GBTC", "DHER.DE", "DIA.MI", "TTNP"]

['MMM', 'ABBN.SW', 'ACLN.SW', 'ACN', 'UDVD.L', 'SPYW.DE', 'IWMO.L', 
'VHYL.SW', 'MVSH.SW', 'CHDVD.SW', 'ADEN.SW', 'XMKA.DE', 'AI.PA', 'AMS.SW', 'AMAT', 
'ASML.AS', 'SAUS.SW', 'BAS.DE', 'CANCDA.SW', 'CAT', 'EMSN.SW', 
'MSE.SW', 'GF.SW', 'F', 'CAC.PA', 'GEBNE.SW', 'XDAX.SW', 'IWDC.SW', 'VWRD.L', 'GT', 
'HOG', 'HON', 'SRECHA.SW', 'IMPN.SW', 'CSMIB.MI', 'DE', 'KMB', 'KNIN.SW', 'AMEL.DE', 
'LONN.SW', 'LCID', 'CSEMAS.SW', 'MAR', 'XLBS.SW', 'CSPXJ.SW', 'PM', 'PHIA.AS', 'PLUG', 
'RIVN', 'SCHN.SW', 'SGSN.SW', 'SIE.SG', '0Z4C.IL', 'SONY', 'XESP.DE', 'SUN.SW', 'CSSMI.SW', 
'CHSPI.SW', 'TKA.F', 'VUSD.L', 'VUKE.L', 'VACN.SW']



SymbTest = ['SIE.SG']

'''["MMM", "ABT", "ABBV", "ACN", "ATVI", "ADBE", "AMD", "AAP", "AES", "AFL", "APD", "AKAM", 
"ALK", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP",
"AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS", "ANTM", "AON", "AOS", "AAPL", "AMAT", "APTV",
"ADM", "ANET", "AJG", "AIZ", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR", "BLL", "BAC", "BBWI", "BAX", "BDX",
"BBY", "BIO", "TECH", "BIIB", "BLK", "BK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BRO", "CHRW",
"CDNS", "CZR", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP",
"CDAY", "CERN", "CF", "CRL", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "CFG", "CTXS",
"CLX", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP", "ED", "STZ", "COO", "CPRT", "GLW", "CTVA",
"COST", "CTRA", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG",
"DLR", "DFS", "DISCA", "DISCK", "DISH", "DG", "DLTR", "DPZ", "DOV", "DOW", "DTE", "DUK", "DRE", "DD", "DXC", "EMN",
"ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR", "ENPH", "ETR", "EOG", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "EVRG",
"ES", "RE", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FB", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FRC", "FISV",
"FLT", "FTNT", "FTV", "FBHS", "FOXA", "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GNRC", "GD", "GE", "GIS", "GM", "GPC",
"GILD", "GL", "GPN", "GS", "GWW", "HAL"]'''
#Symb = ['AMZN', 'GOOG', 'NRT', 'PRT', 'EXTN', 'ERF', 'NEX', 'GLOP', 'VAL', 'EQT', 'KOS', 'DHT', 'ASC', 'MVO', 'AMPY', 'UGP',
#'SLCA', 'CRK', 'TGS', 'CRC', 'RNGR', 'PHX', 'WTTR']
#Symb = ["AVB", "BAX"]

#print("Nb de VALEURS", len(Symb_INDUSTRIEL))

Croiss = []

TablastV = []
TabprelastV = []

Select = []
SelectSymb = []
#inf = 0.6
#sup = 0.8

def take(elem):
    return elem[4]

def Ratio(X, inf, H, h):#, sup):
	for i in X:

		data = yf.Ticker(i)
		df = round(data.history(period="3mo"), 4)
		#print(df)
		L = len(df.index)
		#print(L)
		Tab = [0]*L     #nb de lignes a traiter
		C = 0      		#RATIO jours croissant/decroissant pour premier tri.
		Dend = 0
		D1M = 0
		DENDTXT = "OK"
		#[*, k] ; k=0 ; ouverture, k=1 ; au plus haut, k=2 ; au plus bas, k=3 ; fermeture 
		#print(df.iloc[k, 3], df.iloc[k, 0])

			
		for l in range(H):
			#print (l)
			if (df.iloc[L-(H+1)+l+1, 3] < df.iloc[L-(H+1)+l, 3]) :
			#ICI CHECK FERMETURE D ET D-1

			#(df.iloc[L-(H+1)+l+1, 1] < df.iloc[L-(H+1)+l, 1]) and 
				Dend = Dend+1
				if Dend >= h: 
					#print(i, 'DECROISSANCE RECENTE')
					DENDTXT = "NON"
					break
		#print(Dend, "Dend - jour de decroissance la derniere semaine")


		for k in range (L-1):

			#COMPARAISON FERMETURE - OUVERTURE
			#if df.iloc[k, 3] > df.iloc[k, 0]:	
			#	C = C+1

			#COMPARAISON D et D+1. avec ouverture et fermeture.
			if (df.iloc[k+1, 3] > df.iloc[k, 3]):  
			#ICI CHECK FERMETURE D ET D-1 
			#(df.iloc[k+1, 1] > df.iloc[k, 1]) or 

				C = C+1

			else:
				if k>(2/3)*L:
					D1M = D1M+1


		#print(D1M)
		if (C/L > inf and D1M<inf*(1/3)*L): #() # and (Dend < 3):# and (C/L < sup): # Lim Sup a introduire? si C/L trop élevé ; chances de décroissance
		#print(df)

			Tab = [0]*(L-1)	
			for j in range(L-1):
				Tab[j] = df.iloc[j, 3] 
				#print(Tab)
			Av = statistics.mean(Tab)  #MOYENNE
			sigma =  statistics.stdev(Tab) #ECART TYPE
			Max = max(Tab)
			Min = min(Tab)
			ETN = sigma/(Av)
			Pond = 0
			for j in range(L-1):    #L-1  ############# A PASSER EN L ??
				Pond = Pond + (df.iloc[j+1, 3] - df.iloc[j, 3])
			Pond = Pond/(Max - Min)
			#print (Pond)

		#if Pond > 0:


 						#TEST FAIT SUR LE DERNIER JOUR DU MOIS
		#LastV = [0]*len(Symb)

			#print(Tab)

			#COMPARAISON FERMETURES
		#LastV = df.iloc[L-1, 3]
		#PrelastV = df.iloc[L-2, 3]

			#COMPARAISON FERMETURE - OUVERTURE
			LastV = df.iloc[L-1, 3]
			PrelastV = df.iloc[L-8, 3]    ############ -1 a virer lors du passage en situation reelle
		#print(LastV, PrelastV)

		#print(Tab)
# - Min) #ECART TYPE NORMALISE    =/=    COEFFICIENT DE VARIATION = sigma/Av
		#print(Av, sigma, ETN)
			Croiss.append([i, "            ", DENDTXT, "       ", round(Pond, 4), "ponderation        ", D1M, "D1M"]) #Symbole, difference dans la journee, % de gain/perte, ecart type
		#lastv - prelastv /max - min?
		#TablastV.append([i, lastV])
		#TabprelastV.append([i, lastV])

		#print(Croiss)
			""""""#print("croissante", i)

		else : 
			""""""#print("Pas assez croissante", i, round(C/L, 3), "C/L     ", D1M, "D1M")


			pass


	# take second element for sort


	# sort list with key
	Croiss.sort(key=take)

	for i in range(len(Croiss)):
		print(Croiss[i])

	
		
#Ratio(Symb_INDUSTRIEL, 0.57, 6, 4)#, 0.8)

Ratio(Symb, 0.57, 6, 4)









'''


Croiss.sort(key = lambda x: x[3])  #RANGER PAR ORDRE CROISSANT D ECART TYPE
#for i in range(len(Croiss)):
#	print(Croiss[i])
Select = Croiss[:100]			   # N PREMIERS ELEMENTS DE LA LISTE SELECTIONNES
#print(Croiss)
Neg = 0 
Pos = 0
Prctg = 0
for i in range(len(Select)):
	print(Select[i], 5)
	Prctg = Prctg + Select[i][2] #Somme des pourcentages
	if (Select[i][2] <= 0) :
		Neg = Neg + 1
		#print(Prctg)
	else:
		Pos = Pos + 1
		#print(Select[i][2])
		#print(Prctg)
	#print(Prctg)
Prctg = Prctg/len(Select) # Normalisation du pourcentage
print("Nb croissantes", Pos, "; ", "Nb decroissantes", Neg, "; ", "GAIN POURCENTAGE", round(Prctg, 5), "; ", "INF :", inf, " ,SUP :", sup)


'''






#for i in range(len(Select)):
#	for j in range(len(TablastV)):
#		if Select[i, :] == TablastV[j, :]:

	#SelectSymb[i] = Select[[i][0]] 
#print(SelectSymb)













#print(Amazon.info) 
#A = (Amazon.history(period="1mo"))
#print(A, type(A))
#print(A.iloc[0, 0])
