from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#GOOGLE SPREADSHEET
import gspread
from oauth2client.service_account import ServiceAccountCredentials


import numpy as np

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.



drive = GoogleDrive(gauth)




scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('laboratoireapi-05a61dd84fd1.json', scope)
client = gspread.authorize(creds)






#ensemble des compagnies
Symb=('NRT', 'PRT', 'EXTN', 'ERF', 'SPN', 'GMLP', 'NEX', 'GLOP', 'VAL', 'EQT', 'KOS', 'DHT', 'ASC', 'MVO', 'AMPY', 'UGP', 'GLOG', 'SLCA', 'CRK', 'TGS', 'CTRA', 'CRC', 'RNGR', 'PHX', 'WTTR')
N=len(Symb)
#NameWorksheets = np.zeros(N)

#nombre de jours pour les stats
njr = 19

Tab = np.zeros((njr, N))

spsheet = client.open("API_labo")



#tableau des valeurs de cloture par compagnie
for n in range(N):
	COMP = spsheet.worksheet(Symb[n])
	#print(COMP)
	if COMP.cell(1,2).value != '#N/A': 		#boucle de verification de l'existence des societes
											#si elle n'existe pas : 0 pour ses valeurs dans le tableau

		for k in range(njr) :
			#Tab[n, k] = COMP.acell("F"+str(n+2))
			val = COMP.cell(k+2, 6).value
			val_float = val.replace(',','.')     #changer la virgule en point pour convertir en flottant
			#print(val_float)
			Tab[k, n] = float(val_float)
	else :
		print(COMP.cell(1,1).value)
		Tab[k, n] = 0
print ("==============================================")
print (Tab)
#print (time.strftime("%d/%m/%Y")) #rappel pour la MaJ des dates dans le fichier de creation


#fonction de comptage des compagnies en croissance sur DeltaD
Xdaysup = np.zeros(N) #tableau de comptage

#Ratio
DeltaD = 10 #nombre de jours pris en compte consécutivement

for n in range(N):
	Xdaysup[n] = 1
	for k in range(DeltaD):
		#A = 1
		if Tab[k, n] > Tab[k+1, n] :
			#print (A)
			pass
		else : 
			#A = 0
			Xdaysup[n] = 0
			#print(A)
	#print ("=======")	
	#print (A)
	#Xdaysup[n] = A
print ("==============================================")
print (Xdaysup)   #1 si DeltaD jours de croissance consécutive, 0 sinon.



Ratio = 2/3 #compris entre 1/2 et 1
#fonction de differentiation de croissance/de comptage pour X jours de croissance sur DeltaD jours.
AddT = int(0.5*DeltaD)

RatioBin = np.zeros((DeltaD+AddT, N))
RatioModsin = np.zeros(N)			#modsin car modulé sur le sinus

for n in range(N):
	A = 0
	for k in range(DeltaD):   #RANGE (DELTAD - 1)???????????
		if Tab[k, n] > Tab[k+1, n] :
			RatioBin[k, n] = 1
			A = A + 1
		else : 
			RatioBin[k, n] = 0
	if A/DeltaD >= Ratio :							#si plus grand que 2/3 de hausse/baisse, alors achat.
		RatioModsin[n] = 1
	if (A/DeltaD < Ratio) and (A/DeltaD > 1 - Ratio):
		B = 0
		for a in range(AddT):						#si entre 1/3 et 2/3, alors determination du comportement précédent.
			if Tab[a + DeltaD, n] > Tab[a + DeltaD + 1, n] :
				RatioBin[a + DeltaD, n] = 1
				B = B + 1
			else : 
				RatioBin[a + DeltaD, n] = -1
		if B/AddT >= Ratio : 
			RatioModsin[n] = -1/2   	#maximum local => va decroitre
		if B/AddT <= 1 - Ratio : 
			RatioModsin[n] = 1/2 		#minimum local => va croitre
		else :
			RatioModsin[n] = 0   		#indeterminee
	if (A/DeltaD) <= 1 - Ratio : 
		RatioModsin[n] = 0				#si hausse/baisse < 1/3, alors non achat.



print ("==============================================")
print (RatioBin)
print (RatioModsin)
	#Xdaysup[n] = A



print ("==============================================")
#pourcentage de valeurs haussieres, si depassant un ratio minimal donne : (industrie/medicaments...) ; si tendance croissance, achat sur toutes les valeurs. 
#(favoriser les petites quotations de petites differences entre elles)
#+ modulation par un sinus aussi?
GlobalUp = np.zeros(DeltaD)
Ratio2 = 7/12
for j in range(DeltaD):
	A = 0
	for n in range(N):
		#print (A)
		A = A + RatioBin[j, n]
		#print (A)
		#print (N)
	if A/N >= Ratio2 :
		GlobalUp[j] = A/N
	else : 
		GlobalUp[j] = 0

print(GlobalUp) # pourcentage de societes qui ont ete en hausse sur un domaine choisi.



print ("==============================================")








#fonction faisant une liste des compagnies prealablement selectionnees sur DeltaD
ListCOMPs_up = []
ListCOMPs_diff = []
for n in range (N): 
	if Xdaysup[n] == 0 :
		pass
	else : 
		ListCOMPs_up.append(Symb[n])
for n in range(N):
	if (RatioModsin[n] == 1/2) or (RatioModsin[n] == 1):
		ListCOMPs_diff.append(Symb[n])
print ("==============================================")
print (ListCOMPs_up)
print (ListCOMPs_diff)




