import pandas as pd
import numpy as np

filepath = "https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_minute.csv"

import ssl  # we need to import this library and tweak one setting due to fact we use HTTPS certificate(s)
ssl._create_default_https_context = ssl._create_unverified_context

# Now we want to create a dataframe and use Pandas' to_csv function to read in our file
data = pd.read_csv(filepath, skiprows=1)  # we use skiprows parameter because first row contains our web address
data = np.array(data) #Convert the dataframe into an array in order to iterate thru it

# LABELS
# bos: base order size
# sos: safety order size
# inv: amount invested
# stc: safety trades count
# tp: target profit %
# ip: initial price
# pd: price deviation to open safety orders (% from initial order)

def Backtest(tp,bos,sos,pd,stc):
    ip = 0 #initial price
    fp = 0 #Final profit for the Backtest Strategy
    stu = 0 #Safety trades used
    #count = 0
    for i in reversed(data):    
        #print(i[5],i[6])
        if float(i[5]) > 0 and float(i[6]) > 0:
            low = float(i[5]) #highest price in the interval
            high = float(i[6]) #lowest price in the interval
        else:
            print("Missing values or equal to zero. Program terminated.")
            break
        if ip == 0: #first order
            ip = (low + high) / 2
            inv = bos
            dca = ip
            crypto = bos / ip
        elif high >= dca * ((100 + tp) / 100): #Condition to take profits
            fp += tp/100 * inv
            #print("take profit:",tp/100*inv)
            dca = dca * ((100 + tp) / 100)
            #print("New current DCA:",dca)
            inv = bos
            crypto = bos / dca
            stu = 0
            ip = dca            
        elif low <= ip * ((100 - pd * (1 + stu)) / 100) and stu < stc: #Condition to activate safety trade
            crypto += sos / (ip * ((100 - pd * (1 + stu)) / 100))
            inv += sos
            stu += 1
            dca = inv / crypto
        else: #in any other case do nothing
            pass
    print("Safe Trades Used in current deal:",stu)
    print("Money currently invested:",inv)
    print("Current DCA:",round(dca,2))
    print("Total profit for the period:",round(fp,2))
    #print(count)


Backtest(3.26,10,10,2,30)
