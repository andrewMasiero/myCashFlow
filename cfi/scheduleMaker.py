import cfi
from data.cashFlowConfig import sysConfig
import datetime
from tkinter import *
from tkinter import ttk
import business

class ScheduleMaker(Toplevel):
	def __init__(self, contentFrame, account):
		super().__init__()
		self.title("Schedule Maker")
		self.geometry("250x200")

		keys = sysConfig['scheduleHeadings']
		n = len(keys)
		d = datetime.datetime.now()
		d = d.strftime("%x")
		sVars = [StringVar() for x in keys]
		entryBoxes = []

		for i in range(4):
			self.columnconfigure(i, weight=1)
		for i in range(n+3):
			self.rowconfigure(i, weight=1)

		for i in range(n):
			if keys[i] == 'date':
				sVars[i].set(d)
			else:
				sVars[i].set(sysConfig['defaultSchedule'][i])
			# print(sVars[i].get())
			ttk.Label(self, text=keys[i], padding=(0, 0, 5, 0)).grid(column=1, row=i+1, sticky=E)
			entryBoxes.append(ttk.Entry(self, textvariable=sVars[i], text=keys[i]))
			entryBoxes[i].delete(0, 'end')
			entryBoxes[i].insert(0, sVars[i].get())
			entryBoxes[i].grid(column=2, row=i+1)
			entryBoxes[i].bind('<Return>', lambda e: self.destroy())
		entryBoxes[0].focus()

		# for i in range(len(entryBoxes)):




		cancel = ttk.Button(self, text="Cancel", command=lambda: self.destroy())
		cancel.grid(column=1, row=n+2)

		create = ttk.Button(self, text="Create", command=lambda: self.createSchedule(contentFrame, account, entryBoxes))
		create.grid(column=2, row=n+2)

	def createSchedule(self, contentFrame, account, entryBoxes):
		keys = sysConfig['scheduleHeadings']
		values = [x.get() for x in entryBoxes]
		schedule = {}
		for k, v in zip(keys, values):
			schedule[k] = v
		account.addSchedule(business.Schedule(schedule))

		cfi.displaySchedules(contentFrame, account)

		self.destroy()

		# values = ['fdsa', 'vcxs', 'rewq', 'yuio', 'gfds', 'vcxz']
		# l = label.winfo_children()
		# keys = list(schedule.attributes.keys())
		# keys.pop()
		# for i in range(len(l)):
		# 	l[i].config(text=entryBoxes[i].get())
		# 	schedule.attributes[keys[i]] = entryBoxes[i].get()
		# for name in keys:
		# 	print(schedule.attributes[name])
		# self.destroy()