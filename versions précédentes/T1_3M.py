

import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import statistics

#YAHOOFINANCE

#Symb = ["AAPL", "MSFT", "AMZN", "FB", "GOOGL", "GOOG", "TSLA", "NVDA", "JPM", "JNJ", 
#"UNH", "V", "PG", "HD", "DIS", "MA", "PYPL", "BAC", "ADBE", "PFE", "CMCSA", "CRM", "CSCO",
#"NFLX", "XOM", "VZ", "ABT", "KO", "PEP", "NKE", "TMO", "LLY", "INTC"]

#Symb = ["NVDA"]

#LISTE YUH VALEURS "ENERGIE ET RECOURSSES NATURELLES"
SymbENERGIES_RECOURESSES_NAT = ['ZSIL.SW', 'BHP', 'BKW.SW', 'BP', 'CVX', 'EOAN.DE', 'EDF', 'ENEL.MI', 'ENGI.PA', 'ENI.MI', 'XOM', 'GE', 'GLEN.L', 'ZGLD.SW', 'HOLN.SW', 'RIO.L', 'RWE.DE', 'SHELL.AS', 'TTE.PA', 'VALE', 'VIE.PA']
#VALEURS NON PRISES EN COMPTE : ZSIL(ArgentETF), BKW, ZEROLK, SQBFWU, HYDRTQ, SQBCEU, FISHTQ, RECYTQ
# *100 ; ENEL, RIO
Symb_INDUSTRIEL = ['MMM', 'ABBN.SW', 'ACLN.SW', 'ACN', 'UDVD.L', 'SPYW.DE', 'IWMO.L', 
'VHYL.SW', 'MVSH.SW', 'CHDVD.SW', 'ADEN.SW', 'XMKA.DE', 'AI.PA', 'AMS.SW', 'AMAT', 
'ASML.AS', 'SAUS.SW', 'BAS.DE', 'CANCDA.SW', 'CAT', 'EMSN.SW', 
'MSE.SW', 'GF.SW', 'F', 'CAC.PA', 'GEBNE.SW', 'XDAX.SW', 'IWDC.SW', 'VWRD.L', 'GT', 
'HOG', 'HON', 'SRECHA.SW', 'IMPN.SW', 'CSMIB.MI', 'DE', 'KMB', 'KNIN.SW', 'AMEL.DE', 
'LONN.SW', 'LCID', 'CSEMAS.SW', 'MAR', 'XLBS.SW', 'CSPXJ.SW', 'PM', 'PHIA.AS', 'PLUG', 
'RIVN', 'SCHN.SW', 'SGSN.SW', 'SIE.SG', '0Z4C.IL', 'SONY', 'XESP.DE', 'SUN.SW', 'CSSMI.SW', 
'CHSPI.SW', 'TKA.F', 'VUSD.L', 'VUKE.L', 'VACN.SW']
#*1/100 : BATS.L
#XMBR non trouve # CLN non trouve ; Clariant 0QJS.IL ? # INFR # XNJP
#MMM ?, ACN ?, MSE.SW?
#'XCHA.SW' non comprise par la fonction
SymbTest = ['ZSIL.SW']

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
print("Nb de VALEURS", len(Symb_INDUSTRIEL))

Croiss = []
#CroissA = [] 
#
TablastV = []
TabprelastV = []
#
Select = []
SelectSymb = []
#inf = 0.6
#sup = 0.8

#DEFINIR UNE FONCTION ICI
def Ratio(X, inf, H, h):#, sup):
	for i in X:

		data = yf.Ticker(i)
		df = round(data.history(period="3mo"), 4)
		#print(df)
		L = len(df.index)
		#print(L)
		Tab = [0]*L#nb de lignes a traiter
	#RATIO jours croissant/decroissant pour premier tri.
		C = 0
		Dend = 0
		DENDTXT = "OK"
		#[*, k] ; k=0 ; ouverture, k=1 ; au plus haut, k=2 ; au plus bas, k=3 ; fermeture 

		#print(df.iloc[k, 3], df.iloc[k, 0])

		#CHECK SI TROP DE DECROISSANCE RECENTE (GENRE CHECK 4J SUR LA DERNIERE SEMAINE?) 4 DANGER. 5-6 + ARRET
			
		for l in range(H):
			#print (l)
			if (df.iloc[L-(H+1)+l+1, 3] < df.iloc[L-(H+1)+l, 3]) :
			#ICI CHECK FERMETURE D ET D-1

			#(df.iloc[L-(H+1)+l+1, 1] < df.iloc[L-(H+1)+l, 1]) and 
				Dend = Dend+1
				if Dend >= h: 
					print(i, 'DECROISSANCE RECENTE')
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
			######## DEUX VERIF A FAIRE : OUVERTURE? FERMETURE? ET CHECK SI LES DEUX EN MEME TEMPS

			#AND/OR????
				C = C+1

		
		#else :
		#	D = D+1
	#C = L     
		if (C/L > inf): # and (Dend < 3):# and (C/L < sup): # Lim Sup a introduire? si C/L trop élevé ; chances de décroissance
		#print(df)

			Tab = [0]*(L-1)	
			for j in range(L-1):
				Tab[j] = df.iloc[j, 3] 
			Av = statistics.mean(Tab)  #MOYENNE
			sigma =  statistics.stdev(Tab)#ECART TYPE
			Max = max(Tab)
			Min = min(Tab)
			ETN = sigma/(Av)
			Pond = 0
			for j in range(L-1):    #L-1  ############# A PASSER EN L ??
				Pond = Pond + (df.iloc[j+1, 3] - df.iloc[j, 3])/(Max - Min)

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
			Croiss.append([i, round(LastV - PrelastV, 5),"day0 - day-7,       ", DENDTXT, LastV, PrelastV,  round((LastV - PrelastV)*100/(LastV), 5), "%,       ", round(Pond, 4), "ponderation"]) #Symbole, difference dans la journee, % de gain/perte, ecart type
		#lastv - prelastv /max - min?
		#TablastV.append([i, lastV])
		#TabprelastV.append([i, lastV])

		#print(Croiss)
			print("croissante", i)

		else : 
			print("Pas assez croissante", i)

			pass

	print(Croiss)

	
		
Ratio(Symb_INDUSTRIEL, 0.57, 6, 4)#, 0.8)





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
