from tkinter import *
from tkinter import ttk
from .scheduleEditor import *

class MenuButton(ttk.Frame):
	def __init__(self, parent, name, width):
		super().__init__()
		button = ttk.Button(parent, text=name, width=width)