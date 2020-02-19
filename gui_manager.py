# Allows for Threading GUI and Server/Client

import tkinter as tk
import ledger as lg
import ledger_manager as lm
import random as rand
import server
import guitest as gui

from multiprocessing import Process

def main():
    p = Process(target=server.start())
    q = Process(target=gui.run_gui())
    p.start()
    p.join()
    q.start()
    q.join()

main()