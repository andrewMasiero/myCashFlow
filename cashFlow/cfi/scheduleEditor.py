from tkinter import *
from tkinter import ttk

class ScheduleEditor(Toplevel):
	def __init__(self, label, sVars, schedule):
		super().__init__()
		self.title("Schedule Editor")
		self.geometry("250x200")

		# get names of keys and labels and
		# create StringVars for the values
		names = list(schedule.attributes.keys())
		names.pop()
		n = len(names)
		entryBoxes = []

		# configure columns and rows
		for i in range(4):
			self.columnconfigure(i, weight=1)
		for i in range(n+5):
			self.rowconfigure(i, weight=1)

		# create labels and entry boxes
		for i in range(n):
			ttk.Label(self, text=names[i], padding=(0, 0, 5, 0)).grid(column=1, row=i+1, sticky=E)
			entryBoxes.append(ttk.Entry(self, textvariable=sVars[i]))
			entryBoxes[i].grid(column=2, row=i+1)
			entryBoxes[i].bind('<Return>', lambda e: self.complete(label, sVars, schedule, entryBoxes))
		entryBoxes[0].focus()

		# create cancel and ok buttons
		cancel = ttk.Button(self, text='Cancel', command=lambda: self.destroy())
		cancel.grid(column=1, row=n+3)
		ok = ttk.Button(self, text='OK', command=lambda: self.complete(label, sVars, schedule, entryBoxes))
		ok.grid(column=2, row=n+3)
		ok.bind('<Return>', lambda e: self.complete(label, sVars, schedule, entryBoxes))

	def complete(self, label, sVars, schedule, entryBoxes):
		values = ['fdsa', 'vcxs', 'rewq', 'yuio', 'gfds', 'vcxz']
		l = label.winfo_children()
		names = list(schedule.attributes.keys())
		names.pop()
		for i in range(len(l)):
			# sVars[i].set(entryBoxes[i].get())
			# l[i].config(text=values[i])
			l[i].config(text=entryBoxes[i].get())
			# l[i].config(text=sVars[i].get())
			# schedule.attributes[names[i]] = sVars[i].get()
			schedule.attributes[names[i]] = entryBoxes[i].get()
		for name in names:
			print(schedule.attributes[name])
		self.destroy()