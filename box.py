import numpy as np
import coin
import ledger
import peer

def partition(coinValue, pAvg, systemNumber, totalProcess):
    uProcess = totalProcess/1.1
    iPart = 1
    bool = False
    while(not bool):
        if(uProcess < iPart):
            iPart/1.001
        else:
            bool = True
    


def main():
    print("Jonah is a coward")
    c = coin.Coin(1,1,1)
    c.string()
   

main()