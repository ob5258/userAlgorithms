import LennyStocksAPI
import time
UID = "OB5258"

while 2 > 1:
	LennyStocksAPI.buyStocks(UID, "PRSM", 1)
	time.sleep(300)
	LennyStocksAPI.sellStocks(UID, "VOD", 5)
