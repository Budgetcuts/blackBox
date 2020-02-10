'''from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line'''
from tkinter import *
from tkinter.ttk import *
import tkinter as tk



class Gui:
    def __init__(self):
        self.x = 5
    def window(self):
        window = Tk()
 
        window.title("GitCoin")
        window.geometry("1000x700")
 
        lbl = Label(window, text="GitCoins:", font=("Arial Bold", 16))
        lbl2 = Label(window, text="Average Power", font=("Arial Bold", 16))
        lbl3 = Label(window, text="Number of Machines on the Network", font=("Arial Bold", 16))
        lbl4 = Label(window, text="Personal Computer power", font=("Arial Bold", 16))
 
        lbl.grid(column=0, row=0)
        lbl2.grid(column=8, row=0)
        lbl3.grid(column=0, row=10)
        lbl4.grid(column=8, row=10)
 
        window.mainloop()
        




'''class Gui(App):
    def build(self):

        self.btn = Button(text ='Switch Screen')
        self.btn.bind(on_release=self.click)
        self.btn2 = Button(text ='hi')
        return self.btn

    def click(self, obj):
        self.btn = Button(text = 'Coins:')
        return self.btn


        

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()
'''

