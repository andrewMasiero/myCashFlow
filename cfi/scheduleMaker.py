import datetime
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
		d = datetime.datetime.now()
		d = d.strftime("%x")
		sVars = [StringVar() for x in names]
		values = []
		for i in range(n):
			if names[i] == 'date':
				values.append(d)
				sVars[i].set(d)
			else:
				values.append(names[i])
				sVars[i].set(names[i])
			# print(sVars[i].get())
			ttk.Label(self, text=names[i], padding=(0, 0, 5, 0)).grid(column=1, row=i+1, sticky=E)
			entryBoxes.append(ttk.Entry(self, textvariable=sVars[i], text=names[i]))
			entryBoxes[i].insert(0, sVars[i].get())
			entryBoxes[i].grid(column=2, row=i+1)
			entryBoxes[i].bind('<Return>', lambda e: self.destroy())
		entryBoxes[0].focus()

		# for i in range(len(entryBoxes)):




		cancel = ttk.Button(self, text="Cancel", command=lambda: self.destroy())
		cancel.grid(column=1, row=n+2)

		create = ttk.Button(self, text="Create", command=lambda: self.createSchedule(account, entryBoxes))
		create.grid(column=2, row=n+2)

	def createSchedule(self, account, entryBoxes):
		values = ['fdsa', 'vcxs', 'rewq', 'yuio', 'gfds', 'vcxz']
		self.destroy()