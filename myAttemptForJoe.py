import pandas as pd
import matplotlib.pyplot as plt

nlokDf = pd.read_csv('nlok.csv')
nlokBaseDf = nlokDf

stockAppendingList = ['Df','AssetType','ExcessArray','Capital','SharesOwned']

#Stock array which I iterate over to run the function multiple times in a for loop.
stocks = ['aaplog','amzn','crm','nlok','msft','bdn','cci','eqc','pld','amt','ecl','apd','dd','hun','stld',
          'unh','pfe','abbv','bio','biib','ebay','nke','mcd','f','tsla']

dayAverages=['30']

#Creating base variables with names that are in the stock appending list
#Globals means it is creating global variables so they can be used anywhere
for i in stockAppendingList:
        globals()[f"{i}"]=0

#Making arrays to keep track of the balance for later.

aaplBAL=[]
amznBAL=[]
msftBAL=[]
nlokBAL=[]
crmBAL=[]
bdnBAL=[]
cciBAL=[]
eqcBAL=[]
pldBAL=[]
amtBAL=[]
eclBAL=[]
apdBAL=[]
ddBAL=[]
hunBAL=[]
stldBAL=[]
unhBAL=[]
pfeBAL=[]
abbvBAL=[]
bioBAL=[]
biibBAL=[]
ebayBAL=[]
nkeBAL=[]
mcdBAL=[]
fBAL=[]
tslaBAL=[]
bhaaplBAL=[]
bhamznBAL=[]
bhmsftBAL=[]
bhnlokBAL=[]
bhcrmBAL=[]
bhbdnBAL=[]
bhcciBAL=[]
bheqcBAL=[]
bhpldBAL=[]
bhamtBAL=[]
bheclBAL=[]
bhapdBAL=[]
bhddBAL=[]
bhhunBAL=[]
bhstldBAL=[]
bhunhBAL=[]
bhpfeBAL=[]
bhabbvBAL=[]
bhbioBAL=[]
bhbiibBAL=[]
bhebayBAL=[]
bhnkeBAL=[]
bhmcdBAL=[]
bhfBAL=[]
bhtslaBAL=[]


#This is my buying and selling function    
def stonk(stonkName):
    #Df is the base variable we created earlier using the for loop, it takes in the CSV 
    #Of the stock name that was used as a parameter.
    Df = pd.read_csv(stonkName+'.csv')
    #Sets the starting assetType for each stock to cash and with $10,000 
    AssetType = 'cash'
    ExcessArray = []
    Capital = 10000
    #Start with 0 shares
    SharesOwned = 0
    #Inserting columns into the data frame to keep track of the Worth of the stocks over
    # time
    Df.insert(len(Df.columns),'Balance',Capital)
    Df.insert(len(Df.columns),'Hold',0)
    #Getting the 30 day running average
    Df[stonkName+'30'] = Df['Close'].rolling(window = 30).mean().round(2)    
    #What percent you need to reach to initiate buy
    percentOfRollingDown=0.9 #0.9 !!! DO NOT SET TO 1 !!!
    #What percent the price needs to go up for you to actually sell now
    dropSafeDown=0.85 #0.85
    #What percent you need to reach to initiate sell
    percentOfRollingUp=1.1 #1.1 !!! DO NOT SET TO 1 !!!
    #What percent the price needs to go up for you to actually buy now
    dropSafeUp=1.15 #1.15
    #Getting the shares we can afford on day one to calculate or buy and hold method
    dayOneShares=Capital/Df['Close'][0]
    for x in range(502):
        #Updating the ammount of money we would make with our "Buy and Hold" method each day
        #Based on the ammount of shares we bought on day one and the close price on the day
        Df['Hold'][x]=dayOneShares*Df['Close'][x]
    #Using our 30 day running average (which is why i start at index 29) I calculate whether
    #To buy or sell stock
    for x in range(30-1,len(Df)):
        if(AssetType=='cash'):
            #Todays close = todays Close
            todayClose=Df['Close'].loc[x]
            Df['Balance'][x]=Capital
            #Todays 30avg = todays 30avg
            today30=Df[stonkName+'30'].loc[x]
            #If todays Close is 10% more than the 30 day mean initiate buy
            if(todayClose <= today30*percentOfRollingDown):
                #Excess is the ammount you closed at minus 10% of the rolling avg
                todayExcess = (today30*percentOfRollingDown)-todayClose
                ExcessArray.append(todayExcess)
                if(todayExcess < max(ExcessArray)*dropSafeUp):
                    SharesOwned=(Capital/todayClose)
                    Capital=0
                    AssetType='stocks'
                    ExcessArray = []
        else:
                                            #Todays close = todays Close
            todayClose=Df['Close'].loc[x]
            Df['Balance'][x]=SharesOwned*todayClose                                                                                 #Todays 30avg = todays 30avg
            today30=Df[stonkName+'30'].loc[x]                                     #If todays Close is 10% more than the 30 day mean initiate sell
            if(todayClose <= today30*percentOfRollingUp):
                                                                                        #Excess is the ammount you closed at minus 110% of the rolling avg
                todayExcess = todayClose-(today30*percentOfRollingUp)
                ExcessArray.append(todayExcess)
                if(todayExcess > min(ExcessArray)*dropSafeDown):
                    Capital = (todayClose*SharesOwned)
                    SharesOwned=0
                    AssetType='cash'
                    ExcessArray = []   
                    
    #Creating a dateLine for our x axis to keep track of time for our graph
    balanceX=[]
    for x in nlokBaseDf['Date']:
        balanceX.append(x)
    #Creating a balance for each individual stock to put on our graph
    balanceY = []
    for x in Df['Balance']:
        balanceY.append(x)

    #stockAppendingListArray
    #Using our stock name and our stock appending list, we dynamically create variables
    # to keep track of each stocks different columns and values.
    sALA=[Df,AssetType,ExcessArray,Capital,SharesOwned]
    for i in range(len(stockAppendingList)):
        globals()[f"{stonkName}{stockAppendingList[i]}"] = sALA[i]
            
    #This checks the stock name and adds to the Balance and Hold Balance
    # arrays created earlier so we can graph
    
    ################### TECH
    if(stonkName=='aaplog'):
        for x in range(502):
            aaplBAL.append(Df['Balance'][x])
            bhaaplBAL.append(Df['Hold'][x])
    elif(stonkName=='crm'):
        for x in range(502):
            crmBAL.append(Df['Balance'][x])
            bhcrmBAL.append(Df['Hold'][x])
    elif(stonkName=='msft'):
        for x in range(502):
            msftBAL.append(Df['Balance'][x])
            bhmsftBAL.append(Df['Hold'][x])
    elif(stonkName=='nlok'):
        for x in range(502):
            nlokBAL.append(Df['Balance'][x])
            bhnlokBAL.append(Df['Hold'][x])
    elif(stonkName=='amzn'):
        for x in range(502):
            amznBAL.append(Df['Balance'][x])
            bhamznBAL.append(Df['Balance'][x])
    ################### REAL ESTATE
    elif(stonkName=='bdn'):
        for x in range(502):
            bdnBAL.append(Df['Balance'][x])
            bhbdnBAL.append(Df['Balance'][x])
    elif(stonkName=='cci'):
        for x in range(502):
            cciBAL.append(Df['Balance'][x])
            bhcciBAL.append(Df['Balance'][x])
    elif(stonkName=='eqc'):
        for x in range(502):
            eqcBAL.append(Df['Balance'][x])
            bheqcBAL.append(Df['Balance'][x])            
    elif(stonkName=='pld'):
        for x in range(502):
            pldBAL.append(Df['Balance'][x])
            bhpldBAL.append(Df['Balance'][x])
    elif(stonkName=='amt'):
        for x in range(502):
            amtBAL.append(Df['Balance'][x])
            bhamtBAL.append(Df['Balance'][x])
    ################### MATERIALS
    elif(stonkName=='ecl'):
        for x in range(502):
            eclBAL.append(Df['Balance'][x])
            bheclBAL.append(Df['Balance'][x])
    elif(stonkName=='apd'):
        for x in range(502):
            apdBAL.append(Df['Balance'][x])
            bhapdBAL.append(Df['Balance'][x])     
    elif(stonkName=='dd'):
        for x in range(502):
            ddBAL.append(Df['Balance'][x])
            bhddBAL.append(Df['Balance'][x])
    elif(stonkName=='hun'):
        for x in range(502):
            hunBAL.append(Df['Balance'][x])  
            bhhunBAL.append(Df['Balance'][x])
    elif(stonkName=='stld'):
        for x in range(502):
            stldBAL.append(Df['Balance'][x])
            bhstldBAL.append(Df['Balance'][x])
    ################### HEALTHCARE 
    elif(stonkName=='unh'):
        for x in range(502):
            unhBAL.append(Df['Balance'][x])
            bhunhBAL.append(Df['Balance'][x])
    elif(stonkName=='pfe'):
        for x in range(502):
            pfeBAL.append(Df['Balance'][x])
            bhpfeBAL.append(Df['Balance'][x])
    elif(stonkName=='abbv'):
        for x in range(502):
            abbvBAL.append(Df['Balance'][x])
            bhabbvBAL.append(Df['Balance'][x])
    elif(stonkName=='bio'):
        for x in range(502):
            bioBAL.append(Df['Balance'][x])
            bhbioBAL.append(Df['Balance'][x])
    elif(stonkName=='biib'):
        for x in range(502):
            biibBAL.append(Df['Balance'][x])
            bhbiibBAL.append(Df['Balance'][x])
    ################### CONSUMER DISRETIONARY (CD)
    elif(stonkName=='ebay'):
        for x in range(502):
            ebayBAL.append(Df['Balance'][x])
            bhebayBAL.append(Df['Balance'][x])
    elif(stonkName=='nke'):
        for x in range(502):
            nkeBAL.append(Df['Balance'][x])
            bhnkeBAL.append(Df['Balance'][x])
    elif(stonkName=='mcd'):
        for x in range(502):
            mcdBAL.append(Df['Balance'][x])
            bhmcdBAL.append(Df['Balance'][x])

    elif(stonkName=='f'):
        for x in range(502):
            fBAL.append(Df['Balance'][x])
            bhfBAL.append(Df['Balance'][x])

    elif(stonkName=='tsla'):
        for x in range(502):
            tslaBAL.append(Df['Balance'][x])
            bhtslaBAL.append(Df['Balance'][x])  
            
            
#Running the function which buys and sells stocks in a for loop which iterates over
#all the stocks
for x in stocks:
    stonk(x)

#Adding the daily balances of each stock and then dividing by 5 to find the 
# industry daily average

avgTECHBAL=[]
for x in range(502):
    numToAdd = (amznBAL[x]+aaplBAL[x]+crmBAL[x]+nlokBAL[x]+msftBAL[x])/5
    avgTECHBAL.append(numToAdd)

avgREALESTATEBAL=[]
for x in range(502):
    numToAdd = (eqcBAL[x]+cciBAL[x]+pldBAL[x]+amtBAL[x]+bdnBAL[x])/5
    avgREALESTATEBAL.append(numToAdd)

avgMATERIALSBAL=[]
for x in range(502):
    numToAdd = (eclBAL[x]+apdBAL[x]+ddBAL[x]+hunBAL[x]+stldBAL[x])/5
    avgMATERIALSBAL.append(numToAdd)

avgHEALTHCAREBAL=[]
for x in range(502):
    numToAdd = (unhBAL[x]+pfeBAL[x]+abbvBAL[x]+bioBAL[x]+biibBAL[x])/5
    avgHEALTHCAREBAL.append(numToAdd)

avgCDBAL=[]
for x in range(502):
    numToAdd = (ebayBAL[x]+nkeBAL[x]+mcdBAL[x]+fBAL[x]+tslaBAL[x])/5
    avgCDBAL.append(numToAdd)

#Adding the daily balances of the Hold and Buy method and dividing by 5
# to find the average for each industry

avgTECHHOLD=[]
for x in range(502):
    numToAdd = (bhamznBAL[x]+bhaaplBAL[x]+bhcrmBAL[x]+bhnlokBAL[x]+bhmsftBAL[x])/5
    avgTECHHOLD.append(numToAdd)

avgREALESTATEHOLD=[]
for x in range(502):
    numToAdd = (bheqcBAL[x]+bhcciBAL[x]+bhpldBAL[x]+bhamtBAL[x]+bhbdnBAL[x])/5
    avgREALESTATEHOLD.append(numToAdd)

avgMATERIALSHOLD=[]
for x in range(502):
    numToAdd = (bheclBAL[x]+bhapdBAL[x]+bhddBAL[x]+bhhunBAL[x]+bhstldBAL[x])/5
    avgMATERIALSHOLD.append(numToAdd)

avgHEALTHCAREHOLD=[]
for x in range(502):
    numToAdd = (bhunhBAL[x]+bhpfeBAL[x]+bhabbvBAL[x]+bhbioBAL[x]+bhbiibBAL[x])/5
    avgHEALTHCAREHOLD.append(numToAdd)

avgCDHOLD=[]
for x in range(502):
    numToAdd = (bhebayBAL[x]+bhnkeBAL[x]+bhmcdBAL[x]+bhfBAL[x]+bhtslaBAL[x])/5
    avgCDHOLD.append(numToAdd)

#creating an x axis time line for our graph
dateHolder = []
for x in nlokDf['Date']:
    dateHolder.append(x)

#Plotting each industry on one graph with labels to indentify
plt.plot(dateHolder,avgTECHBAL,label="TECH")
plt.plot(dateHolder,avgREALESTATEBAL,label="REAL ESTATE")
plt.plot(dateHolder,avgMATERIALSBAL,label="MATERIALS")
plt.plot(dateHolder,avgHEALTHCAREBAL,label="HEALTHCARE")
plt.plot(dateHolder,avgCDBAL,label="CD")

#Setting up the graph visually
#The rotation of the x axis
plt.xticks(dateHolder,rotation=31-1)
#The ammount of ticks on the x axis
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance Average Market Stocks")
plt.xlabel("Months(2)")
plt.legend()
plt.title("Market 30 Day Running Averages")
plt.show()

#Same process as above but for the Buy and Hold Model
plt.plot(dateHolder,avgTECHHOLD,label="TECH")
plt.plot(dateHolder,avgREALESTATEHOLD,label="REAL ESTATE")
plt.plot(dateHolder,avgMATERIALSHOLD,label="MATERIALS")
plt.plot(dateHolder,avgHEALTHCAREHOLD,label="HEALTHCARE")
plt.plot(dateHolder,avgCDHOLD,label="CD")

plt.xticks(dateHolder,rotation=30)
plt.locator_params(axis='x',nbins=12)
plt.ylabel("Balance Average Market Stocks")
plt.xlabel("Months(2)")
plt.legend()
plt.title("Buy and Hold day One")
plt.show()