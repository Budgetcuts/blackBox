import numpy as np
import coin
import ledger
import peer
import gui



def partition(coinValue, pAvg, systemNumber, totalProcess):
    uProcess = totalProcess/1.1
    iPart = 1
    bool = False
    while(not bool):
        if(uProcess < iPart):
            iPart/1.001
        else:
            bool = True
    

def update():
        myCoin = coin.Coin(1,1,1)
        t = gui.Gui()
        t.window()
        
        #btn = Button(text ='Switch Screen')
        #x`btn.bind(on_release=)
        #btn2 = Button(text ='hi')
       



def main():

    c = coin.Coin(1,1,1)
    c.string()
    update()
   

main()