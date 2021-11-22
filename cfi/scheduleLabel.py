from tkinter import *
from tkinter import ttk
from .scheduleEditor import *

class ScheduleLabel(ttk.Frame):
	def __init__(self, parent, schedule):
		super().__init__()
		
		values = schedule.attributes
		names = list(values.keys())
		names.pop()
		widths = [15, 25, 25, 20, 10]
		sVars = [StringVar() for x in names]
		
		c = {'Credit': "light green", 'Debit': 'light pink'}
		c = c[schedule.attributes['paymentType']]
		s = ttk.Style()
		s.configure('schedule.TFrame', background="dark gray")
		
		for i in range(len(names)):
			sVars[i].set(values[names[i]])
			l = ttk.Label(self, text=sVars[i].get(), background=c, width=widths[i], borderwidth=1, relief='solid')
			l.grid(column=i, row=0)
			# l.bind('<Double-ButtonPress-1>', lambda e: self.complete(sVars, schedule))
			l.bind('<Double-ButtonPress-1>', lambda e: ScheduleEditor(self, sVars, schedule))
		self.grid()