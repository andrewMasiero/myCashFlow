from tkinter import *
from tkinter import ttk

class ScheduleEditor(Toplevel):
	def __init__(self, contentFrame, label, schedule):
		super().__init__()
		self.title("Schedule Editor")
		self.geometry("250x200")

		# get names of keys and labels and
		# create StringVars for the values
		keys = list(schedule.attributes.keys())
		keys.pop()
		n = len(keys)
		entryBoxes = []
		sVars = [StringVar() for k in keys]
		l = [x for x in label.winfo_children()]
		
		# configure columns and rows
		for i in range(4):
			self.columnconfigure(i, weight=1)
		for i in range(n+5):
			self.rowconfigure(i, weight=1)

		# create labels and entry boxes
		for i in range(n):
			sVars[i].set(l[i]['text'])
			ttk.Label(self, text=keys[i], padding=(0, 0, 5, 0)).grid(column=1, row=i+1, sticky=E)
			entryBoxes.append(ttk.Entry(self, textvariable=sVars[i]))
			entryBoxes[i].grid(column=2, row=i+1)
			entryBoxes[i].bind('<Return>', lambda e: self.complete(label, schedule, entryBoxes, sVars))
		entryBoxes[0].focus()

		# create cancel and ok buttons
		cancel = ttk.Button(self, text='Cancel', command=lambda: self.destroy())
		cancel.grid(column=1, row=n+3)
		ok = ttk.Button(self, text='OK', command=lambda: self.complete(label, schedule, entryBoxes, sVars))
		ok.grid(column=2, row=n+3)
		ok.bind('<Return>', lambda e: self.complete(label, schedule, entryBoxes))

	def complete(self, label, schedule, entryBoxes, sVars):
		values = ['fdsa', 'vcxs', 'rewq', 'yuio', 'gfds', 'vcxz']
		l = label.winfo_children()
		keys = list(schedule.attributes.keys())
		keys.pop()
		for i in range(len(l)):
			l[i].config(text=entryBoxes[i].get())
			schedule.attributes[keys[i]] = entryBoxes[i].get()
		for key in keys:
			print(schedule.attributes[key])
		self.destroy()