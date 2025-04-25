

import numpy as np
import pandas_datareader as pdr
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

#YAHOOFINANCE
Symb = ['AMZN']

Amazon = yf.Ticker("AMZN")
#print(Amazon.info) 
A = (Amazon.history(period="1mo"))
print(A, type(A))
print(A.iloc[0, 0])
#CA MAAARCHE






#TIINGO
#data = pdr.get_data_tiingo('GOOG', api_key='b6f0eb455814196897784855eb270ae2362670ed')
#print(data)

#IEX
#f = web.DataReader('F', 'pk_4da351d3d78c45db865c506a196130e5', '2018-08-31', '2018-09-10')
#print(f)
"""
Symb = ('GOOG')#, 'ABT')
#Symb=('NRT', 'PRT', 'EXTN', 'ERF', 'SPN', 'GMLP', 'NEX', 'GLOP', 'VAL', 'EQT', 'KOS', 'DHT', 'ASC', 'MVO', 'AMPY', 'UGP', 'GLOG', 'SLCA', 'CRK', 'TGS', 'CTRA', 'CRC', 'RNGR', 'PHX', 'WTTR')


start_date = '2016-12-25'
end_date = '2016-12-31'

A = len(Symb)
print(A)

#Data = np.zeros(range(A))

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
#for i in range(len(Symb)) :
Data = data.DataReader(Symb, 'google', start_date, end_date)    
#yahoo peut etre a changer en google ou autre service
print (Data)
print (Data.iloc[1, 1])    #atteindre la valeur dans le tableau cree par pandas
"""

'''

Attributes   Adj Close                  Close                   High                    Low                   Open              Volume          
Symbols           GOOG        ABT        GOOG        ABT        GOOG        ABT        GOOG        ABT        GOOG        ABT     GOOG       ABT
Date                                                                                                                                            
2016-12-15  797.849976  36.597557  797.849976  38.930000  803.000000  39.049999  792.919983  38.270000  797.340027  38.759998  1626500   9229400
2016-12-16  790.799988  35.817284  790.799988  38.099998  800.856018  39.330002  790.289978  37.980000  800.400024  39.020000  2443800  15107500
2016-12-19  794.200012  36.042900  794.200012  38.340000  797.659973  38.630001  786.270020  38.060001  790.219971  38.230000  1232100  10153500

'''
#DATES ET HEADER NON PRIS EN COMPTE DANS L INDEXATION.
#COURS DE FERMETURE EN (L,C) = (1, 1) pour la premiere  (j 1)
#							 = (1, 2) pour la deuxieme	(j 1)
#							 = (1, 3) pour la troisieme	(j 1)
#					         = (Njr, NCie)  iteration lineraire commencant en (1,1)






