# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:00:58 2020

@author: Colin
"""

#amzn nlok crm msft

import pandas as pd
import locale
import matplotlib.pyplot as plt
import numpy as np

locale.setlocale( locale.LC_ALL, '' )

nlokDf = pd.read_csv('nlok.csv')

aaplDf = pd.read_csv('UPDATEDNOTORIGINAL.csv')
# aaplaaplDf['apl30'] = aaplDf['Close'].rolling(window = 30).mean().round(2)
aaplAssetType = 'cash'
yesterdayExcess = 0
aaplExcessArray = []
aaplCapital = 10000
startingAaplCapital = aaplCapital
aaplSharesOwned = 0
# aaplDf.insert(2,'Balance',aaplCapital)
#What percent you need to reach to initiate buy
percentOfRollingDown=0.9 #0.9 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually sell now
dropSafeDown=0.85 #0.85
#What percent you need to reach to initiate sell
percentOfRollingUp=1.1 #1.1 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually buy now
dropSafeUp=1.15 #1.15
aaplBuyCount = 0
aaplSellCount = 0

for x in range(29,len(aaplDf)):
    if(aaplAssetType=='cash'):
        #Todays close = todays Close
        todayClose=aaplDf['Close'].loc[x]
        aaplDf['Balance'][x]=aaplCapital
        #Todays 30avg = todays 30avg
        today30=aaplDf['apl30'].loc[x]
        #If todays Close is 10% more than the 30 day mean initiate buy
        if(todayClose <= today30*percentOfRollingDown):
            #Excess is the ammount you closed at minus 10% of the rolling avg
            todayExcess = (today30*percentOfRollingDown)-todayClose
            aaplExcessArray.append(todayExcess)
            if(todayExcess < max(aaplExcessArray)*dropSafeUp):
                aaplSharesOwned=(aaplCapital/todayClose)
                #print("   SPENT " + str(locale.currency(aaplCapital,grouping=True)) + " for  " + str(aaplSharesOwned.round(2)) + " shares " + str(x))
                aaplCapital=0
                aaplAssetType='stocks'
                aaplExcessArray = []
                aaplBuyCount+=1
    else:
                                        #Todays close = todays Close
        todayClose=aaplDf['Close'].loc[x]
        aaplDf['Balance'][x]=aaplSharesOwned*todayClose                                                                                 #Todays 30avg = todays 30avg
        today30=aaplDf['apl30'].loc[x]                                     #If todays Close is 10% more than the 30 day mean initiate sell
        if(todayClose <= today30*percentOfRollingUp):
                                                                                    #Excess is the ammount you closed at minus 110% of the rolling avg
            todayExcess = todayClose-(today30*percentOfRollingUp)
            aaplExcessArray.append(todayExcess)
            if(todayExcess > min(aaplExcessArray)*dropSafeDown):
                aaplCapital = (todayClose*aaplSharesOwned)
                #print("RETURNED " + str(locale.currency(aaplCapital,grouping=True)) + " from " + str(aaplSharesOwned.round(2))+" shares\n" + str(x))
                aaplSharesOwned=0
                aaplAssetType='cash'
                aaplExcessArray = []  
                aaplSellCount += 1

balanceX=[]
for x in nlokDf['Date']:
    balanceX.append(x)

balanceY = []
for x in aaplDf['Balance']:
    balanceY.append(x)


'''
plt.plot(balanceX,balanceY,label='aapl')

plt.xticks(balanceX,rotation=30)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance")
plt.xlabel("Months(2)")
plt.title("AAPL INVESTMENT TRACKER - $10,000")
plt.show()
'''
###############################MSFT
msftDf = pd.read_csv('msft.csv')
msftDf['msft30'] = msftDf['Close'].rolling(window = 30).mean().round(2)
msftAssetType = 'cash'
yesterdayExcess = 0
msftExcessArray = []
msftCapital = 10000
startingmsftCapital = msftCapital
msftSharesOwned = 0
msftDf.insert(2,'Balance',msftCapital)
#What percent you need to reach to initiate buy
percentOfRollingDown=0.9 #0.9 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually sell now
dropSafeDown=0.85 #0.85
#What percent you need to reach to initiate sell
percentOfRollingUp=1.1 #1.1 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually buy now
dropSafeUp=1.15 #1.15
msftBuyCount = 0
msftSellCount = 0

for x in range(29,len(msftDf)):
    if(msftAssetType=='cash'):
        #Todays close = todays Close
        todayClose=msftDf['Close'].loc[x]
        msftDf['Balance'][x]=msftCapital
        #Todays 30avg = todays 30avg
        today30=msftDf['msft30'].loc[x]
        #If todays Close is 10% more than the 30 day mean initiate buy
        if(todayClose <= today30*percentOfRollingDown):
            #Excess is the ammount you closed at minus 10% of the rolling avg
            todayExcess = (today30*percentOfRollingDown)-todayClose
            msftExcessArray.append(todayExcess)
            if(todayExcess < max(msftExcessArray)*dropSafeUp):
                msftSharesOwned=(msftCapital/todayClose)
                #print("   SPENT " + str(locale.currency(msftCapital,grouping=True)) + " for  " + str(msftSharesOwned.round(2)) + " shares " + str(x))
                msftCapital=0
                msftAssetType='stocks'
                msftExcessArray = []
                msftBuyCount+=1
    else:
                                        #Todays close = todays Close
        todayClose=msftDf['Close'].loc[x]
        msftDf['Balance'][x]=msftSharesOwned*todayClose                                                                                 #Todays 30avg = todays 30avg
        today30=msftDf['msft30'].loc[x]                                     #If todays Close is 10% more than the 30 day mean initiate sell
        if(todayClose <= today30*percentOfRollingUp):
                                                                                    #Excess is the ammount you closed at minus 110% of the rolling avg
            todayExcess = todayClose-(today30*percentOfRollingUp)
            msftExcessArray.append(todayExcess)
            if(todayExcess > min(msftExcessArray)*dropSafeDown):
                msftCapital = (todayClose*msftSharesOwned)
                #print("RETURNED " + str(locale.currency(msftCapital,grouping=True)) + " from " + str(msftSharesOwned.round(2))+" shares " + str(x))
                msftSharesOwned=0
                msftAssetType='cash'
                msftExcessArray = []  
                msftSellCount += 1

balanceX=[]
for x in msftDf['Date']:
    balanceX.append(x)

balanceY = []
for x in msftDf['Balance']:
    balanceY.append(x)
    
plt.plot(balanceX,balanceY,label='msft')

'''
plt.plot(balanceX,balanceY)
plt.xticks(balanceX,rotation=30)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance")
plt.xlabel("Months(2)")
plt.title("msft INVESTMENT TRACKER - $10,000")
plt.show()
'''
###############################CRM
crmDf = pd.read_csv('crm.csv')
crmDf['crm30'] = crmDf['Close'].rolling(window = 30).mean().round(2)
crmAssetType = 'cash'
yesterdayExcess = 0
crmExcessArray = []
crmCapital = 10000
startingcrmCapital = crmCapital
crmSharesOwned = 0
crmDf.insert(2,'Balance',crmCapital)
#What percent you need to reach to initiate buy
percentOfRollingDown=0.9 #0.9 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually sell now
dropSafeDown=0.85 #0.85
#What percent you need to reach to initiate sell
percentOfRollingUp=1.1 #1.1 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually buy now
dropSafeUp=1.15 #1.15
crmBuyCount = 0
crmSellCount = 0

for x in range(29,len(crmDf)):
    if(crmAssetType=='cash'):
        #Todays close = todays Close
        todayClose=crmDf['Close'].loc[x]
        crmDf['Balance'][x]=crmCapital
        #Todays 30avg = todays 30avg
        today30=crmDf['crm30'].loc[x]
        #If todays Close is 10% more than the 30 day mean initiate buy
        if(todayClose <= today30*percentOfRollingDown):
            #Excess is the ammount you closed at minus 10% of the rolling avg
            todayExcess = (today30*percentOfRollingDown)-todayClose
            crmExcessArray.append(todayExcess)
            if(todayExcess < max(crmExcessArray)*dropSafeUp):
                crmSharesOwned=(crmCapital/todayClose)
                #print("   SPENT " + str(locale.currency(crmCapital,grouping=True)) + " for  " + str(crmSharesOwned.round(2)) + " shares " + str(x))
                crmCapital=0
                crmAssetType='stocks'
                crmExcessArray = []
                crmBuyCount+=1
    else:
                                        #Todays close = todays Close
        todayClose=crmDf['Close'].loc[x]
        crmDf['Balance'][x]=crmSharesOwned*todayClose                                                                                 #Todays 30avg = todays 30avg
        today30=crmDf['crm30'].loc[x]                                     #If todays Close is 10% more than the 30 day mean initiate sell
        if(todayClose <= today30*percentOfRollingUp):
                                                                                    #Excess is the ammount you closed at minus 110% of the rolling avg
            todayExcess = todayClose-(today30*percentOfRollingUp)
            crmExcessArray.append(todayExcess)
            if(todayExcess > min(crmExcessArray)*dropSafeDown):
                crmCapital = (todayClose*crmSharesOwned)
                #print("RETURNED " + str(locale.currency(crmCapital,grouping=True)) + " from " + str(crmSharesOwned.round(2))+" shares " + str(x))
                crmSharesOwned=0
                crmAssetType='cash'
                crmExcessArray = []  
                crmSellCount += 1

balanceX=[]
for x in crmDf['Date']:
    balanceX.append(x)

balanceY = []
for x in crmDf['Balance']:
    balanceY.append(x)
    
plt.plot(balanceX,balanceY,label='crm')
'''

plt.plot(balanceX,balanceY)
plt.xticks(balanceX,rotation=30)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance")
plt.xlabel("Months(2)")
plt.title("CRM INVESTMENT TRACKER - $10,000")
plt.show()
'''
###############################amzn
amznDf = pd.read_csv('amzn.csv')
amznDf['amzn30'] = amznDf['Close'].rolling(window = 30).mean().round(2)
amznAssetType = 'cash'
yesterdayExcess = 0
amznExcessArray = []
amznCapital = 10000
startingamznCapital = amznCapital
amznSharesOwned = 0
amznDf.insert(2,'Balance',amznCapital)
#What percent you need to reach to initiate buy
percentOfRollingDown=0.9 #0.9 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually sell now
dropSafeDown=0.85 #0.85
#What percent you need to reach to initiate sell
percentOfRollingUp=1.1 #1.1 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually buy now
dropSafeUp=1.15 #1.15
amznBuyCount = 0
amznSellCount = 0

for x in range(29,len(amznDf)):
    if(amznAssetType=='cash'):
        #Todays close = todays Close
        todayClose=amznDf['Close'].loc[x]
        amznDf['Balance'][x]=amznCapital
        #Todays 30avg = todays 30avg
        today30=amznDf['amzn30'].loc[x]
        #If todays Close is 10% more than the 30 day mean initiate buy
        if(todayClose <= today30*percentOfRollingDown):
            #Excess is the ammount you closed at minus 10% of the rolling avg
            todayExcess = (today30*percentOfRollingDown)-todayClose
            amznExcessArray.append(todayExcess)
            if(todayExcess < max(amznExcessArray)*dropSafeUp):
                amznSharesOwned=(amznCapital/todayClose)
                #print("   SPENT " + str(locale.currency(amznCapital,grouping=True)) + " for  " + str(amznSharesOwned.round(2)) + " shares " + str(x))
                amznCapital=0
                amznAssetType='stocks'
                amznExcessArray = []
                amznBuyCount+=1
    else:
                                        #Todays close = todays Close
        todayClose=amznDf['Close'].loc[x]
        amznDf['Balance'][x]=amznSharesOwned*todayClose                                                                                 #Todays 30avg = todays 30avg
        today30=amznDf['amzn30'].loc[x]                                     #If todays Close is 10% more than the 30 day mean initiate sell
        if(todayClose <= today30*percentOfRollingUp):
                                                                                    #Excess is the ammount you closed at minus 110% of the rolling avg
            todayExcess = todayClose-(today30*percentOfRollingUp)
            amznExcessArray.append(todayExcess)
            if(todayExcess > min(amznExcessArray)*dropSafeDown):
                amznCapital = (todayClose*amznSharesOwned)
                #print("RETURNED " + str(locale.currency(amznCapital,grouping=True)) + " from " + str(amznSharesOwned.round(2))+" shares " + str(x))
                amznSharesOwned=0
                amznAssetType='cash'
                amznExcessArray = []  
                amznSellCount += 1

balanceX=[]
for x in amznDf['Date']:
    balanceX.append(x)

balanceY = []
for x in amznDf['Balance']:
    balanceY.append(x)
    
plt.plot(balanceX,balanceY,label='amzn')
'''
plt.plot(balanceX,balanceY)
plt.xticks(balanceX,rotation=30)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance")
plt.xlabel("Months(2)")
plt.title("amzn INVESTMENT TRACKER - $10,000")
plt.show()
'''
###############################nlok
# Located Uptop
# nlokDf = pd.read_csv('nlok.csv')
nlokDf['nlok30'] = nlokDf['Close'].rolling(window = 30).mean().round(2)
nlokAssetType = 'cash'
yesterdayExcess = 0
nlokExcessArray = []
nlokCapital = 10000
startingnlokCapital = nlokCapital
nlokSharesOwned = 0
nlokDf.insert(2,'Balance',nlokCapital)
#What percent you need to reach to initiate buy
percentOfRollingDown=0.9 #0.9 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually sell now
dropSafeDown=0.85 #0.85
#What percent you need to reach to initiate sell
percentOfRollingUp=1.1 #1.1 !!! DO NOT SET TO 1 !!!
#What percent the price needs to go up for you to actually buy now
dropSafeUp=1.15 #1.15
nlokBuyCount = 0
nlokSellCount = 0

for x in range(29,len(nlokDf)):
    if(nlokAssetType=='cash'):
        #Todays close = todays Close
        todayClose=nlokDf['Close'].loc[x]
        nlokDf['Balance'][x]=nlokCapital
        #Todays 30avg = todays 30avg
        today30=nlokDf['nlok30'].loc[x]
        #If todays Close is 10% more than the 30 day mean initiate buy
        if(todayClose <= today30*percentOfRollingDown):
            #Excess is the ammount you closed at minus 10% of the rolling avg
            todayExcess = (today30*percentOfRollingDown)-todayClose
            nlokExcessArray.append(todayExcess)
            if(todayExcess < max(nlokExcessArray)*dropSafeUp):
                nlokSharesOwned=(nlokCapital/todayClose)
                #print("   SPENT " + str(locale.currency(nlokCapital,grouping=True)) + " for  " + str(nlokSharesOwned.round(2)) + " shares " + str(x))
                nlokCapital=0
                nlokAssetType='stocks'
                nlokExcessArray = []
                nlokBuyCount+=1
    else:
                                        #Todays close = todays Close
        todayClose=nlokDf['Close'].loc[x]
        nlokDf['Balance'][x]=nlokSharesOwned*todayClose                                                                                 #Todays 30avg = todays 30avg
        today30=nlokDf['nlok30'].loc[x]                                     #If todays Close is 10% more than the 30 day mean initiate sell
        if(todayClose <= today30*percentOfRollingUp):
                                                                                    #Excess is the ammount you closed at minus 110% of the rolling avg
            todayExcess = todayClose-(today30*percentOfRollingUp)
            nlokExcessArray.append(todayExcess)
            if(todayExcess > min(nlokExcessArray)*dropSafeDown):
                nlokCapital = (todayClose*nlokSharesOwned)
                #print("RETURNED " + str(locale.currency(nlokCapital,grouping=True)) + " from " + str(nlokSharesOwned.round(2))+" shares " + str(x))
                nlokSharesOwned=0
                nlokAssetType='cash'
                nlokExcessArray = []  
                nlokSellCount += 1

balanceX=[]
for x in nlokDf['Date']:
    balanceX.append(x)

balanceY = []
for x in nlokDf['Balance']:
    balanceY.append(x)
    
plt.plot(balanceX,balanceY, label='nlok')
'''
plt.plot(balanceX,balanceY)
plt.xticks(balanceX,rotation=30)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance")
plt.xlabel("Months(2)")
plt.title("nlok INVESTMENT TRACKER - $10,000")
plt.show()
'''


AVERAGEFORALL=[]
for x in range(502):
    numToAdd = (aaplDf['Balance'][x] + msftDf['Balance'][x] + nlokDf['Balance'][x] + crmDf['Balance'][x] + amznDf['Balance'][x])/5
    AVERAGEFORALL.append(numToAdd)

dateHolder=[]
for x in nlokDf['Date']:
    dateHolder.append(x)
    

plt.plot(dateHolder,AVERAGEFORALL,label='THE REAL ALL')
plt.xticks(dateHolder,rotation=30)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance Average Tech Stocks")
plt.xlabel("Months(2)")
plt.title("Tech Market Average Balance")
plt.legend()
plt.figure(figsize=(30,20),dpi=60)
plt.show()


#print("Over the course of " + str(len(msftDf['Close']))+ " days, you bought " + str(msftBuyCount) + " times and sold " + str(msftSellCount) + " times. \nYour money is currently held in " + msftAssetType + "\n")
#print("You started with " + str(locale.currency((startingmsftCapital),grouping=True)) + "\nYou ended with   " + str(locale.currency((msftCapital),grouping=True)) + "\nYour profits are " + str(locale.currency((msftCapital-startingmsftCapital),grouping=True)))


        
                
                
    
    

