#Code by Isaac Chadirchi
#Last Updated 25/05/17

#!/usr/bin/python
import traderFunctionsPrivate
import MySQLdb
import time
import math
import decimal

buy = "buy"
sell = "sell"

#Public Func
def getUserBalance(UID):
	db, cur = traderFunctionsPrivate.openDatabase()
	balance = traderFunctionsPrivate.balanceLookUp(db, cur, UID)
	traderFunctionsPrivate.closeDatabase(db)
	return balance

#Public Func
def getStockPrices(companyCode):
	db, cur = traderFunctionsPrivate.openDatabase()
	stockPrice = traderFunctionsPrivate.lookUpStockPrices(db, cur, companyCode)
	traderFunctionsPrivate.closeDatabase(db)
	return stockPrice

#Public Func
def getTransactionFee(companyCode):
	db, cur = traderFunctionsPrivate.openDatabase()
	transactionFee = traderFunctionsPrivate.lookUpTransactionFee(db, cur, companyCode)
	traderFunctionsPrivate.closeDatabase(db)
	return transactionFee

#Public Func
def getUserOwnedStocks(UID, companyCode):
	db, cur = traderFunctionsPrivate.openDatabase()
	ownedStocks = traderFunctionsPrivate.lookUpOwnedStocks(db, cur, UID, companyCode)
	traderFunctionsPrivate.closeDatabase(db)
	return ownedStocks

#Public Func
def buyFunction(UID, companyCode, stockAmount):
	db, cur = traderFunctionsPrivate.openDatabase()
	balance = traderFunctionsPrivate.balanceLookUp(db, cur, UID)
	stockPrice, totalPrice, newBalance = traderFunctionsPrivate.totalPriceCalc(db, cur, companyCode, stockAmount, buy, balance)	
	newOwnedStocks = traderFunctionsPrivate.ownedStocksCalc(db, cur, UID, companyCode, stockAmount, buy)
	if newBalance < 0:
		errorCode = ("ERROR 101: Cannot afford Purchase")
		print errorCode
	elif newBalance >= 0:
		traderFunctionsPrivate.transactionActual(db, cur, UID, companyCode, stockAmount, stockPrice, newBalance, newOwnedStocks)
		print "You have bought",stockAmount,"stocks in",companyCode,"at a price of",stockPrice,"GBx each, for a total of",(-totalPrice),"GBx.\nYou now have a balance of",newBalance,"GBx, and own",newOwnedStocks,"stocks in",companyCode
	return

#Public Func
def sellFunction(UID, companyCode, stockAmount):
	db, cur = traderFunctionsPrivate.openDatabase()
	balance = traderFunctionsPrivate.balanceLookUp(db, cur, UID)
	stockPrice, totalPrice, newBalance = traderFunctionsPrivate.totalPriceCalc(db, cur, companyCode, stockAmount, sell, balance)
	newOwnedStocks = traderFunctionsPrivate.ownedStocksCalc(db, cur, UID, companyCode, stockAmount, sell)
	if newOwnedStocks < 0:
		errorCode = ("ERROR 102: Do not own enough stocks")
		print errorCode
	elif newOwnedStocks >= 0:
		traderFunctionsPrivate.transactionActual(db, cur, UID, companyCode, stockAmount, stockPrice, newBalance, newOwnedStocks)
		print "You have sold",stockAmount,"stocks in",companyCode,"at a price of",stockPrice,"GBx each, for a total of",totalPrice,"GBx.\nYou now have a balance of",newBalance,"GBx, and own",newOwnedStocks,"stocks in",companyCode
	return

#Public Func
def getCompanyCode(CID):
	db, cur = traderFunctionsPrivate.openDatabase()
	companyCode = traderFunctionsPrivate.lookUpCompanyCode(db, cur, CID)
	traderFunctionsPrivate.closeDatabase(db)
	return companyCode
	
#Public Func
def getCompanyName(companyCode):
	db, cur = traderFunctionsPrivate.openDatabase()
	companyName = traderFunctionsPrivate.lookUpCompanyName(db, cur, companyCode)
	traderFunctionsPrivate.closeDatabase(db)
	return companyName

#Public Func
def getPriceChange(companyCode):
	db, cur = traderFunctionsPrivate.openDatabase()
	priceChange = traderFunctionsPrivate.lookUpPriceChange(db, cur, companyCode)
	traderFunctionsPrivate.closeDatabase(db)
	return priceChange
