try:
    from tkinter import *
except ImportError:
    from Tkinter import *


def init(canvas_width, canvas_height):
    global root
    root = Tk()
    global canvas
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()
