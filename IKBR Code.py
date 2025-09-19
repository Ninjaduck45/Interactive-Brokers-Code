from ib_insync import IB, Stock, util
import time
import sys
import CustomFunctions



ib = IB() # Class instance of our connection, stores all the data for our specific case

HOST = '' #Your machine adress 
PORT = 4001 #4001 for IB Gateway Live Trading
CLIENT_ID = 1

SPYHistoricalData = CustomFunctions.getHistoricalData("Spy", "1m", "5d", "SPYHistoricalData") #Downloads the historical data as a csv file



ib.connect(HOST, PORT, clientId=1)
contract = Stock('SPY', 'SMART', 'USD')


while True:


    retryAttemps = 0
    if CustomFunctions.conTest(ib) != True: #Checks to see if the API is still connected by asking for the time

        print("Connection Lost")
        time.sleep(15)
        print("Attempting to Reconnect")

        while CustomFunctions.conTest(ib) != True:

            try:
                ib.connect(HOST, PORT, clientId=1) #Attempts to reconnect, then goes to the except if an error is thrown
            except: 
                print("Connection Failed, Retrying")
                time.sleep(15)

                retryAttemps = retryAttemps + 1
                if retryAttemps >= 10:
                    CustomFunctions.sendAlert("10 Attemps Exceded, Terminating Program, We should go see what happened")
                    print("Terminating Program")
                    sys.exit()
        
        
    else:
        currentTime = time.strftime("%H:%M:%S") 
        time.localtime()
        print("Connected @", currentTime)
  

    time.sleep(60) #Runs every 60 seconds while the program is active