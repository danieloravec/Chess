try:
    from tkinter import *
except ImportError:
    from Tkinter import *


def init():
    global root
    root = Tk()
    global canvas
    canvas = Canvas(root, width=256, height=256)
    canvas.pack()
