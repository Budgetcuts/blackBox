import numpy as np
import coin
import ledger
import peer
import gui

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


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
        #t = gui.Gui()
        #t.run()
        btn = Button(text ='Switch Screen')
        #btn.bind(on_release=)
        btn2 = Button(text ='hi')
       



def main():

    c = coin.Coin(1,1,1)
    c.string()
    update()
   

main()