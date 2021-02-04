import pandas as pd

aaplDf = pd.read_csv('aapl.csv')

'''Rember to give data on initial capital/ equal weights'''
Capital = 9000

apple_capital = 1000
apple_shares = 0
apple_asset_type = 'cash or stocks'

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


#################   Buying Logic   #######################################     ############   notes   ########################           
#initiating purchase

def buyAppleStock(day,assetType,aaplCap):   
    while aaplDf['Close'][day] <= buy_limit: 
        print(buy_limit)
        aaplDf['trailing buy'][day] = (aaplDf['Close'][day] - buy_limit)                        
        if aaplDf['trailing buy'][day]>= 1.15*aaplDf['trailing buy'].max():
            assetType = 'cash'
            if assetType != 'stocks':
                print("GET")
                apple_shares = apple_capital/aaplDf['Close'][day]
                assetType = 'stocks'
                day += 1
                
                #    is entered that is 15% above the min value in
                

######### BUYING CRITERIA
for x in range(len(aaplDf)):
    if aaplDf['30 day Buy Criteria'][x] == True:
        if apple_asset_type != 'stocks':
            buy_limit = aaplDf['Close'][x]
            #If the close price raises 15% above the minimim value in 
            #the list after the trailing stop is triggered
            if aaplDf['Close'][x] >= 1.15*aaplDf['buy limit'][x].max():
                buyAppleStock(x,apple_asset_type,apple_capital)
                

def sellAppleStock(day,assetType,aaplCap):    
    while aaplDf['Close'][day+1] >= sell_limit:  
        aaplDf['trailing sell'].append(aaplDf['Close'][day] - sell_limit)                        
        if aaplDf['trailing sell'][day] <= 0.85*aaplDf['trailing sell'].floor():
            if assetType != 'cash':
                apple_capital = apple_shares*aaplDf['Close'][day]
                assetType = 'cash'                                                                    

######### SELLING CRITERIA
for x in range(len(aaplDf)):
    if aaplDf['30 day Sell Criteria'][x] == True:
        if apple_asset_type != 'cash':
            aaplDf['sell limit'][x] = aaplDf['Close'][x]
            if aaplDf['Close'][x] <= 0.85*aaplDf['sell limit'][x].min():
                apple_capital =apple_shares*aaplDf['Close']
                apple_asset_type = 'cash'                
                sellAppleStock(x,apple_asset_type,apple_capital)

        

#################   Selling Logic   #######################################    ############   notes   ########################            
#initiating sale
'''
aaplDf['30 day Sell Criteria'] = aaplDf['Close'] >= aaplDf['aaplMoving30']*1.1 ####indicates if the price rises 10% above the sma 
if aaplDf['30 day Sell Criteria'] = true:
aaplDf['Close'] = sell_limit                                                   #### sets current price to var sell_limit
while value in aaplDf['Close'] > sell_limit:
    aaplDf['trailing sell'].append(value - sell_limit)                         #### appends the difference of the values above the 
    for num in aaplDf['trailing sell']:                                        #sell_limit into a list
        if num <= 0.85*aaplDf['trailing sell'].max():                          #### executes sale when a value in the list is
                                                                               #entered that is 15% below the  max value in the 
                                                                               #list
# executing sale

            if apple_asset_type != 'cash':
                apple_capital = aapple_shares*aaplDf['Close']
                apple_asset_type = 'cash'''




# #################   Buying Logic   #######################################     ############   notes   ########################           
# #initiating purchase

# def buyAppleStock(day,assetType,aaplCap):
#     aaplDf['30 day Buy Criteria'] = aaplDf['Close'] <= aaplDf['aaplMoving30']*0.9  ####indicates if the price falls 10% below the sma 
#     if aaplDf['30 day Buy Criteria'] == True:
#         aaplDf['Close'] = sell_limit                                                   #### sets current price to var buy_limit
#     while aaplDf['Close'][day] > sell_limit:
#         aaplDf['trailing sell'].append(aaplDf['Close'][day] - sell_limit)                         #### appends the difenence of the values above the 
#         for num in aaplDf['trailing sell']:                                        #buy_limit into a list
#             if num <= 0.85*aaplDf['trailing sell'].max():                          #### executes purchase when a value in the list 
#                 if assetType != 'cash':
#                     apple_capital = apple_shares*aaplDf['Close']
#                     assetType = 'cash'
#                 #    is entered that is 15% above the min value in
#                                                                                #    the list
