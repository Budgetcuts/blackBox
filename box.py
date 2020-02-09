import numpy as np
import coin
import ledger
import peer
import gui

from kivy.app import App
from kivy.uix.button import Button


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
    while(True):
        myCoin = coin.Coin(1,1,1)



def main():

    t = gui.Gui()
    t.run()
    c = coin.Coin(1,1,1)
    c.string()
    update()
   

main()