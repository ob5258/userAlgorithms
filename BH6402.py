#Code by Ben Hirschfield
#Last Updated 25/05/17

#!/usr/bin/python
import LennyStocksAPI
import MySQLdb
import math
import decimal
import time
	
booleanVar = 1

userID = ("BH6402")
stockID = ("TSLA")

#loop start
while (booleanVar == 1):
	
	myint = 1
	
	compCode = stockID
	abPrice = LennyStocksAPI.getPrice(compCode)
	feeVar = LennyStocksAPI.getFee(compCode)
	print "Company:",compCode,"\t Price per Stock (GBx):",abPrice,"\t Transaction Fee (GBx):",feeVar
	
	balance = LennyStocksAPI.getBalance(userID)
	print "Balance (GBx):",balance
	
        if balance > 10:
                s_amount = (balance - feeVar)/abPrice
                finalAmount = math.floor(s_amount)
		intFinalAmount = int(finalAmount)
		#print intFinalAmount
        else :
                booleanVar = 0
	
	if (finalAmount < 1):
                booleanVar = 0
        else:
                strVAR1 = str(compCode)
                strFinalAmount = str(finalAmount)
                strVAR2 = str(abPrice)
		
		time.sleep(1)
		
                #Buying Stocks
                
		LennyStocksAPI.buyStocks(userID, strVAR1, intFinalAmount)
		
		time.sleep(1)
		
                #Selling Stocks
		
		stockAmount = LennyStocksAPI.getOwnedStocks(userID, strVAR1)
		#print stockAmount
		
		LennyStocksAPI.sellStocks(userID, strVAR1, stockAmount)
		
		time.sleep(1)



