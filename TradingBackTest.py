import csv
import numpy as np

#The csv file was downloaded from this URL: https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_minute.csv
#The csv file order has been inverted: from oldest to newest in order to test it
    
with open(r'C:\Users\corte\Documents\Binance_BTCUSDT_minute.csv') as f: 
    data = list(csv.reader(f, delimiter=","))

 
data = np.array(data)
data = data[~np.all(data == '', axis=1)]

#dca: dollar cost-average
#bos: Base Order Size
#sos: Safety Order Size
#crypto: amount of crypto invested
#inv: amount invested
#stc: safety trades count
#tp: target profit %
#ip: initial price
#pd: price deviation to open safety orders (% from initial order)
#low: lowest price of the inversal (minute)
#high: highest price of the interval (minute)

def Backtest(tp,bos,sos,pd,stc):
    ip = 0 #initial price
    fp = 0 #Final profit for the Backtest Strategy
    stu = 0 #Safety trades used
    for i in data:    
        #print(i[6],i[5])
        if float(i[6]) > 0 and float(i[5]) > 0:
            low = float(i[5])
            high = float(i[6])
        else:
            print("Missing values or equal to zero. Program terminated.")
            break
        if ip == 0: #first order
            ip = (low + high) / 2
            inv = bos
            dca = ip
            crypto = bos / ip
        elif high >= dca * ((100 + tp)/100): #Condition to take profits
            fp += tp/100 * inv
            dca = dca * ((100 + tp)/100)
            inv = bos
            crypto = bos / dca
            stu = 0
            ip = dca
            #print(fp)
        elif low <= ip * ((100 - pd*(1+stu))/100) and stu < stc: #Condition to activate safety trade
            crypto += sos / (ip * ((100 - pd*(1+stu))/100))
            inv += sos
            stu += 1
            dca = inv / crypto
            #print(dca)
        else: #in any other case do nothing
            pass
    print("Total profit for the period:",round(fp,2))
    #print(count)

Backtest(2,20,20,2,15)
