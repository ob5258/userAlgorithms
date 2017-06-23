import LennyStocksAPI
import time

from datetime import datetime, time
now = datetime.now()

UID = "JS1234"

while 1 > 0:
	LennyStocksAPI.buyStocks(UID, "AAPL", 2)
	time.sleep(600)
	LennyStocksAPI.sellStocks(UID, "AAPL", 2)
	
	

	
