import LennyStocksAPI
import MySQLdb
import math
import decimal
import time

userID = ("JP1337")
stockID = ("TSLA")
	
	compCode = stockID
	abPrice = LennyStocksAPI.getPrice(compCode)
	feeVar = LennyStocksAPI.getFee(compCode)
	print "Company:",compCode,"\t Price per Stock:",abPrice,"\t Transaction Fee:",feeVar
	
	balance = LennyStocksAPI.getBalance(userID)
	print "Balance:",balance
	
s_amount = (balance - feeVar)/abPrice
finalAmount = math.floor(s_amount)
intFinalAmount = int(finalAmount)
#print intFinalAmount
   
buySellFunction.sellFunction(userID, stockID, intFinalAmount)
