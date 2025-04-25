
import yfinance as yf

#API implementation/execution

msft = yf.Ticker("OXY")
msft.info
hist = msft.history(period="1mo")
print(hist)
print(type(hist))
for j in range(10):
	print(hist.iloc[j, 3])
#print(msft.history_metadata)

msft.actions
msft.dividends
msft.splits
# show share count
msft.get_shares_full(start="2022-01-01", end=None)




#affichage/comparaison qualite des donnees









