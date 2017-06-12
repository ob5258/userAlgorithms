#Code by Isaac Chadirchi
#Last Updated 25/05/17

#!/usr/bin/python
import sys
sys.path.insert(0, '/home/pi/Trading/functions')

import traderFunctionsPublic

def getBalance(UID):
	balance = traderFunctionsPublic.getUserBalance(UID)
	return balance

def getPrice(companyCode):
	stockPrice = traderFunctionsPublic.getStockPrices(companyCode)
	return stockPrice

def getFee(companyCode):
	transactionFee = traderFunctionsPublic.getTransactionFee(companyCode)
	return transactionFee

def getOwnedStocks(UID, companyCode):
	ownedStocks = traderFunctionsPublic.getUserOwnedStocks(UID, companyCode)
	return ownedStocks

def buyStocks(UID, companyCode, stockAmount):
	traderFunctionsPublic.buyFunction(UID, companyCode, stockAmount)
	return

def sellStocks(UID, companyCode, stockAmount):
	traderFunctionsPublic.sellFunction(UID, companyCode, stockAmount)
	return

def getCompanyCode(CID):
	companyCode = traderFunctionsPublic.getCompanyCode(CID)
	return companyCode

def getCompanyName(companyCode):
	companyName = traderFunctionsPublic.getCompanyName(companyCode)
	return companyName

def getPriceChange(companyCode):
	priceChange = traderFunctionsPublic.getPriceChange(companyCode)
	return priceChange

