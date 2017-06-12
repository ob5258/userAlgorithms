import LennyStocksAPI

UID = "IC5572"
companyCodes = []
companyNames = []
stockPrices = []
priceChanges = []

def displayUserInfo():
	balance = LennyStocksAPI.getBalance(UID)
	

def getAllCompanyInfo():
	for register in range(1, 23):
		companyCodes.append(LennyStocksAPI.getCompanyCode(register))
		#companyNames.append(LennyStocksAPI.getCompanyName(companyCodes[register-1]))
		stockPrices.append(LennyStocksAPI.getPrice(companyCodes[register-1]))
		priceChanges.append(LennyStocksAPI.getPriceChange(companyCodes[register-1]))
		print companyCodes[register-1],"\tPrice per Stock:",stockPrices[register-1],"GBx\tPrice Change:",priceChanges[register-1]

#register = 0
#while register < 22:
	#companyCode = companyCodeList[register]
	#stockPrice = LennyStocksAPI.getPrice(companyCode)
	#transacFee = LennyStocksAPI.getFee(companyCode)
	#stockPricesList.append(stockPrice)
	#transacFeeList.append(transacFee)
	#print "Company:",companyCodeList[register],"\tPrice per Stock (GBx):",stockPricesList[register],"\tTransaction Fee (GBx):",transacFeeList[register]
	#register = register + 1

getAllCompanyInfo()

LennyStocksAPI.buyStocks(UID, "CSCO", 7)
