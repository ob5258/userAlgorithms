#!/usr/bin/python
import MySQLdb
import time
import math
import decimal

buy = "buy"
sell = "sell"

#Private Func
def openDatabase():
	db = MySQLdb.connect(host="localhost", user="root", passwd="tommy", db="Trading")
	cur = db.cursor()
	return db, cur

#Private Func
def balanceLookUp(db, cur, UID):
	cur.execute("SELECT balance FROM Users WHERE UID='{}'".format(UID))
	for row in cur.fetchall():
		balance = row[0]
	return balance

#Private Func
def lookUpStockPrices(db, cur, companyCode):
	cur.execute("SELECT absolutePrice FROM stockPrices WHERE companyCode = '{}'".format(companyCode))
	for row in cur.fetchall():
		stockPrice = row[0]
	return stockPrice

#Private Func
def lookUpTransactionFee(db, cur, companyCode):
	cur.execute("SELECT fee FROM stockPrices WHERE companyCode = '{}'".format(companyCode))
	for row in cur.fetchall():
		transactionFee = row[0]
	return transactionFee

#Private Func
def totalPriceCalc(db, cur, companyCode, stockAmount, buySell, balance):
	stockPrice = lookUpStockPrices(db, cur, companyCode)
	transactionFee = lookUpTransactionFee(db, cur, companyCode)
	if buySell==buy:
		totalPrice = -(stockAmount * stockPrice + transactionFee)
	elif buySell==sell:
		totalPrice = (stockAmount * stockPrice - transactionFee)
	newBalance = balance + totalPrice
	return stockPrice, totalPrice, newBalance

#Private Func
def lookUpOwnedStocks(db, cur, UID, companyCode):
	cur.execute("SELECT {} FROM userStock WHERE UID = '{}'".format(companyCode, UID))
	for row in cur.fetchall():
		ownedStocks = row[0]
	return ownedStocks

#Private Func
def ownedStocksCalc(db, cur, UID, companyCode, stockAmount, buySell):
	ownedStocks = lookUpOwnedStocks(db, cur, UID, companyCode)
	if buySell==buy:
		newOwnedStocks = ownedStocks + stockAmount
	elif buySell==sell:
		newOwnedStocks = ownedStocks - stockAmount
	return newOwnedStocks

#Private Func
def transactionActual(db, cur, UID, companyCode, stockAmount, stockPrice, newBalance, newOwnedStocks):
	cur.execute("INSERT INTO Transactions (UID, time, stock, s_Amount, price) VALUES ('{}', CURTIME(), '{}', {}, {})".format(UID, companyCode, stockAmount, stockPrice))
	cur.execute("UPDATE userStock SET {} = {} WHERE UID = '{}'".format(companyCode, newOwnedStocks, UID))
	cur.execute("UPDATE Users SET balance = {} WHERE UID = '{}'".format(newBalance, UID))
	closeDatabase(db)
	return

#Private Func
def lookUpCompanyCode(db, cur, CID):
	cur.execute("SELECT companyCode FROM stockPrices WHERE CID = '{}'".format(CID))
	for row in  cur.fetchall():
		companyCode = row[0]
	return companyCode

#Private Func
def lookUpCompanyName(db, cur, companyCode):
	cur.execute("SELECT companyName FROM stockPrices WHERE companyCode = '{}'".format(companyCode))
	for row in cur.fetchall():
		companyName = row[0]
	return companyName

#Private Func
def lookUpPriceChange(db, cur, companyCode):
	cur.execute("SELECT priceChange FROM stockPrices WHERE companyCode = '{}'".format(companyCode))
	for row in cur.fetchall():
		priceChange = row[0]
	return priceChange

#Private Func
def closeDatabase(db):
	db.commit()
	db.close()
	return
