import pandas as pd
import locale
import matplotlib.pyplot as plt
import numpy as np

locale.setlocale( locale.LC_ALL, '' )

nlokDf = pd.read_csv('nlok.csv')
nlokBaseDf = nlokDf

stockAppendingList = ['Df','AssetType','ExcessArray','Capital','SharesOwned']

################### ADD STOCK TO STOCKS ARRAY
stocks = ['aaplog','amzn','crm','nlok','msft','bdn','cci','eqc','pld','amt','ecl','apd','dd','hun','stld',
          'unh','pfe','abbv','bio','biib','ebay','nke','mcd','f','tsla']


#100 day average

dayAverages=['100']

for i in stockAppendingList:
    globals()[f"{i}"]=0

################## MAKE A BALANCE
#TECH
aaplBAL=[]
amznBAL=[]
msftBAL=[]
nlokBAL=[]
crmBAL=[]

#REIT
bdnBAL=[]
cciBAL=[]
eqcBAL=[]
pldBAL=[]
amtBAL=[]

#MATERIALS
eclBAL=[]
apdBAL=[]
ddBAL=[]
hunBAL=[]
stldBAL=[]

#Healthcare
unhBAL=[]
pfeBAL=[]
abbvBAL=[]
bioBAL=[]
biibBAL=[]

#Consumer Discretionary (CD)
ebayBAL=[]
nkeBAL=[]
mcdBAL=[]
fBAL=[]
tslaBAL=[]


def stonk(stonkName):
    Df = pd.read_csv(stonkName+'.csv')
    AssetType = 'cash'
    ExcessArray = []
    Capital = 10000
    SharesOwned = 0
    Df.insert(len(Df.columns),'Balance',Capital)
    Df[stonkName+'100'] = Df['Close'].rolling(window = 100).mean().round(2)
    
    #What percent you need to reach to initiate buy
    percentOfRollingDown=0.9 #0.9 !!! DO NOT SET TO 1 !!!
    #What percent the price needs to go up for you to actually sell now
    dropSafeDown=0.85 #0.85
    #What percent you need to reach to initiate sell
    percentOfRollingUp=1.1 #1.1 !!! DO NOT SET TO 1 !!!
    #What percent the price needs to go up for you to actually buy now
    dropSafeUp=1.15 #1.15
    
    for x in range(100-1,len(Df)):
        if(AssetType=='cash'):
            #Todays close = todays Close
            todayClose=Df['Close'].loc[x]
            Df['Balance'][x]=Capital
            #Todays 100avg = todays 100avg
            today100=Df[stonkName+'100'].loc[x]
            #If todays Close is 10% more than the 100 day mean initiate buy
            if(todayClose <= today100*percentOfRollingDown):
                #Excess is the ammount you closed at minus 10% of the rolling avg
                todayExcess = (today100*percentOfRollingDown)-todayClose
                ExcessArray.append(todayExcess)
                if(todayExcess < max(ExcessArray)*dropSafeUp):
                    SharesOwned=(Capital/todayClose)
                    #print("   SPENT " + str(locale.currency(Capital,grouping=True)) + " for  " + str(SharesOwned.round(2)) + " shares " + str(x))
                    Capital=0
                    AssetType='stocks'
                    ExcessArray = []
        else:
            #Todays close = todays Close
            todayClose=Df['Close'].loc[x]
            Df['Balance'][x]=SharesOwned*todayClose                                                                                 #Todays 100avg = todays 100avg
            today100=Df[stonkName+'100'].loc[x]                                     #If todays Close is 10% more than the 100 day mean initiate sell
            if(todayClose <= today100*percentOfRollingUp):
                #Excess is the ammount you closed at minus 110% of the rolling avg
                todayExcess = todayClose-(today100*percentOfRollingUp)
                ExcessArray.append(todayExcess)
                if(todayExcess > min(ExcessArray)*dropSafeDown):
                    Capital = (todayClose*SharesOwned)
                    #print("RETURNED " + str(locale.currency(Capital,grouping=True)) + " from " + str(SharesOwned.round(2))+" shares\n" + str(x))
                    SharesOwned=0
                    AssetType='cash'
                    ExcessArray = []


balanceX=[]
for x in nlokBaseDf['Date']:
    balanceX.append(x)
    
    balanceY = []
    for x in Df['Balance']:
        balanceY.append(x)

#Graph individual stocks
#plt.plot(balanceX,balanceY,label=stonkName)

#stockAppendingListArray
sALA=[Df,AssetType,ExcessArray,Capital,SharesOwned]
for i in range(len(stockAppendingList)):
    globals()[f"{stonkName}{stockAppendingList[i]}"] = sALA[i]
    
    
    
    if(stonkName=='aapl'):
        for x in range(502):
            aaplBAL.append(Df['Balance'][x])
    elif(stonkName=='crm'):
        for x in range(502):
            crmBAL.append(Df['Balance'][x])
elif(stonkName=='msft'):
    for x in range(502):
        msftBAL.append(Df['Balance'][x])
    elif(stonkName=='nlok'):
        for x in range(502):
            nlokBAL.append(Df['Balance'][x])
    elif(stonkName=='amzn'):
        for x in range(502):
            amznBAL.append(Df['Balance'][x])
################### REAL ESTATE
elif(stonkName=='bdn'):
    for x in range(502):
        bdnBAL.append(Df['Balance'][x])
    elif(stonkName=='cci'):
        for x in range(502):
            cciBAL.append(Df['Balance'][x])
    elif(stonkName=='eqc'):
        for x in range(502):
            eqcBAL.append(Df['Balance'][x])
elif(stonkName=='pld'):
    for x in range(502):
        pldBAL.append(Df['Balance'][x])
    elif(stonkName=='amt'):
        for x in range(502):
            amtBAL.append(Df['Balance'][x])
    ######

################### MATERIALS
elif(stonkName=='ecl'):
    for x in range(502):
        eclBAL.append(Df['Balance'][x])
    elif(stonkName=='apd'):
        for x in range(502):
            apdBAL.append(Df['Balance'][x])
    elif(stonkName=='dd'):
        for x in range(502):
            ddBAL.append(Df['Balance'][x])
elif(stonkName=='hun'):
    for x in range(502):
        hunBAL.append(Df['Balance'][x])
    elif(stonkName=='stld'):
        for x in range(502):
            stldBAL.append(Df['Balance'][x])
    ######
################### HEALTHCARE
elif(stonkName=='unh'):
    for x in range(502):
        unhBAL.append(Df['Balance'][x])
    elif(stonkName=='pfe'):
        for x in range(502):
            pfeBAL.append(Df['Balance'][x])
    elif(stonkName=='abbv'):
        for x in range(502):
            abbvBAL.append(Df['Balance'][x])
elif(stonkName=='bio'):
    for x in range(502):
        bioBAL.append(Df['Balance'][x])
    elif(stonkName=='biib'):
        for x in range(502):
            biibBAL.append(Df['Balance'][x])
    ######
################### CONSUMER DISRETIONARY (CD)
elif(stonkName=='ebay'):
    for x in range(502):
        ebayBAL.append(Df['Balance'][x])
    elif(stonkName=='nke'):
        for x in range(502):
            nkeBAL.append(Df['Balance'][x])
    elif(stonkName=='mcd'):
        for x in range(502):
            mcdBAL.append(Df['Balance'][x])
elif(stonkName=='f'):
    for x in range(502):
        fBAL.append(Df['Balance'][x])
    elif(stonkName=='tsla'):
        for x in range(502):
            tslaBAL.append(Df['Balance'][x])
######


###SKIP
for x in stocks:
    stonk(x)
###


########

AVGTECHBAL=[]
for x in range(502):
    numToAdd = (amznBAL[x]+aaplBAL[x]+crmBAL[x]+nlokBAL[x]+msftBAL[x])/5
    AVGTECHBAL.append(numToAdd)

AVGREALESTATEBAL=[]
for x in range(502):
    numToAdd = (eqcBAL[x]+cciBAL[x]+pldBAL[x]+amtBAL[x]+bdnBAL[x])/5
    AVGREALESTATEBAL.append(numToAdd)

AVGMATERIALSBAL=[]
for x in range(502):
    numToAdd = (eclBAL[x]+apdBAL[x]+ddBAL[x]+hunBAL[x]+stldBAL[x])/5
    AVGMATERIALSBAL.append(numToAdd)

AVGHEALTHCAREBAL=[]
for x in range(502):
    numToAdd = (unhBAL[x]+pfeBAL[x]+abbvBAL[x]+bioBAL[x]+biibBAL[x])/5
    AVGHEALTHCAREBAL.append(numToAdd)

AVGCDBAL=[]
for x in range(502):
    numToAdd = (ebayBAL[x]+nkeBAL[x]+mcdBAL[x]+fBAL[x]+tslaBAL[x])/5
    AVGCDBAL.append(numToAdd)

dateHolder = []
for x in nlokDf['Date']:
    dateHolder.append(x)


plt.plot(dateHolder,AVGTECHBAL,label="TECH")
plt.plot(dateHolder,AVGREALESTATEBAL,label="REAL ESTATE")

plt.plot(dateHolder,AVGMATERIALSBAL,label="MATERIALS")
plt.plot(dateHolder,AVGHEALTHCAREBAL,label="HEALTHCARE")
plt.plot(dateHolder,AVGCDBAL,label="CD")

plt.xticks(dateHolder,rotation=50)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Total Average Market Balance")
plt.xlabel("Date")
plt.suptitle('Test 100 Day SMA MODEL', fontsize=20)
plt.legend()
plt.show()
plt.savefig('Test 100 Day SMA MODEL')
