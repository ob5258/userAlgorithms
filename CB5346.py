import LennyStocksAPI
import time
UID = "CB5346"
while 1 > 0:
  LennyStocksAPI.buyStocks(UID, "AAPL", 2)
  time.sleep(600)
  LennyStocksAPI.sellStocks(UID, "AAPL", 2)
