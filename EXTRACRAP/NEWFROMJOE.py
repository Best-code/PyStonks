
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
#matplotlib inline

aaplDf = pd.read_csv('aapl.csv')

'''Rember to give data on initial capital/ equal weights'''
Capital = 9000

apple_capital = 1000
apple_shares = 0
apple_asset_type = 'cash'

sell_limit = 0
buy_limit = 0
#Initiates simple moving average (sma) columns
aaplDf['aaplMoving30'] = aaplDf['Close'].rolling(window = 30).mean().round(2)
aaplDf['aaplMoving7'] = aaplDf['Close'].rolling(window = 7).mean().round(2)
aaplDf['aaplMoving3'] = aaplDf['Close'].rolling(window = 3).mean().round(2)

##################  30 day  ######################################

##################  Initiates criteria  ######################################

#Initiate sell signal if the close price is at least 10% greater than the sma
aaplDf['30 day Sell Criteria'] = aaplDf['Close'] >= aaplDf['aaplMoving30']*1.1

#Initiate buy signal if the close price is at least 10% less than the sma
aaplDf['30 day Buy Criteria'] = aaplDf['Close'] <= aaplDf['aaplMoving30']*0.9

#creating Buy limit

aaplDf.insert(7,"buy limit",0)

#creating trailing buy

aaplDf.insert(8,"trailing buy",0)

#creating sell limit

aaplDf.insert(9,"sell limit",0)
#creating trailing sell

aaplDf.insert(10,"trailing sell",0)


##################  Trailing stops ######################################
##################   BUY (convert cash to stocks) #########################################

#initiating trailing buy
aaplDf['trailing buy']


####### BUYING ####### BUYING ####### BUYING ####### BUYING ####### BUYING ####### BUYING ####### BUYING ####
####### BUYING ####### BUYING ####### BUYING ####### BUYING ####### BUYING ####### BUYING ####### BUYING ####

#################   Buying Execution

######## Executing the buy ticket
def buyAppleStock(day):
    global apple_asset_type
    if apple_asset_type != 'stocks':
        apple_shares = apple_capital/aaplDf['Close'][day]
        apple_asset_type = 'stocks'
        day += 1
        print("i bought a stock")

#    is entered that is 15% above the min value in

buyLim=[]
######## (Buy) trailing stop
def buyTrailingStop(day,buy_limit):
    while aaplDf['Close'][day] <= 1.15* buy_limit:
        buyLim.append(aaplDf['Close'][day])
        buy_limit = min(buyLim)
        day += 1
    buyAppleStock(day)


######### CRITERIA to initiate buy ticket
for day in range(len(aaplDf)):
    if aaplDf['30 day Buy Criteria'][day] == True:
        if apple_asset_type != 'stocks':
            buy_limit = aaplDf['Close'][day]
            #If the close price raises 15% above the minimim value in
            #the list after the trailing stop is triggered
            buyTrailingStop(day,buy_limit)



####### SELLING ####### SELLING ####### SELLING ####### SELLING ####### SELLING ####### SELLING ####### SELLING ####
####### SELLING ####### SELLING ####### SELLING ####### SELLING ####### SELLING ####### SELLING ####### SELLING ####
######### Selling execution
# def sellAppleStock(day,assetType):
#     if assetType != 'cash':
#         apple_capital = apple_shares*aaplDf['Close'][day]
#         assetType = 'cash'
#         day += 1

#    is entered that is 15% above the min value in

# sellLim=[]
# ######## (Sell) trailing stop
# def sellTrailingStop(day,sell_limit):
#     while aaplDf['Close'][day] >= 0.85* sell_limit:
#         sellLim.append(aaplDf['Close'][day])
#         sell_limit = min(sellLim)
#         day += 1
#     sellAppleStock(day,'stocks')


# ######### CRITERIA to initiate buy ticket
# for day in range(len(aaplDf)):
#     if aaplDf['30 day Sell Criteria'][day] == True:
#         if apple_asset_type != 'cash':
#             sell_limit = aaplDf['Close'][day]
#             #If the close price raises 15% above the minimim value in
#             #the list after the trailing stop is triggered
#             sellTrailingStop(day,sell_limit)

# aaplDf
