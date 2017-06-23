import LennyStocksAPI
import time

from datetime import datetime, time
now = datetime.now()

UID = "JS1234"

while 1 > 0:
	now_time = now.time()
	if now_time >= time(9,30) and now_time <=(9,35):				
		LennyStocksAPI.buyStocks(UID, "AAPL", 2)
		time.sleep(600)
	if now_time >= time(15,30) and now_time <=(15,35):
		LennyStocksAPI.sellStocks(UID, "AAPL", 2)
	
	

	
