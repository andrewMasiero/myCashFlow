from tkinter import *
from tkinter import ttk

class ScheduleMaker(Toplevel):
	def __init__(self, account):
		super().__init__()
		self.title("Schedule Maker")
		self.geometry("250x200")
		names = ["name", "payee", "amount", "frequency", "date", "paymentType"]
		n = len(names)
		for i in range(4):
			self.columnconfigure(i, weight=1)
		for i in range(n+3):
			self.rowconfigure(i, weight=1)
		entryBoxes = []
		sVars = [StringVar().set(x) for x in names]
		for i in range(n):
			ttk.Label(self, text=names[i], padding=(0, 0, 5, 0)).grid(column=1, row=i+1, sticky=E)
			entryBoxes.append(ttk.Entry(self, textvariable=sVars[i]))
			entryBoxes[i].grid(column=2, row=i+1)
			entryBoxes[i].bind('<Return>', lambda e: self.destroy())
		entryBoxes[0].focus()


		cancel = ttk.Button(self, text="Cancel", command=lambda: self.destroy())
		cancel.grid(column=1, row=n+2)

		create = ttk.Button(self, text="Create", command=lambda: self.destroy())
		create.grid(column=2, row=n+2)