from .scheduleMaker import ScheduleMaker
from .menuButton import MenuButton
import locale
from .scheduleEditor import *
import pyautogui
from tkinter import *
from tkinter import ttk

locale.setlocale(locale.LC_ALL, '')

def getScreenSize():
	s = ''
	res = pyautogui.size()
	w = str(int((res[0]/2) * .60))
	h = str(int(res[1] * .60))
	s += w + 'x' + h + '+0+0'
	return s

def createMainWindow():
	r = Tk()
	r.title("My Cash Flow")
	r.geometry(getScreenSize())
	r.columnconfigure(0, weight=1)
	r.columnconfigure(1, weight=8)
	r.columnconfigure(2, weight=1)
	# r.rowconfigure(0, weight=1)
	# r.rowconfigure(1, weight=9)

	return r

def createFrame(parent, col, row, pad):
	s = ttk.Style()
	s.configure('cf.TFrame', background="dark gray")
	f = ttk.Frame(parent, padding=pad, style='cf.TFrame')
	f.grid(column=col, row=row)
	return f

def addButtonsHorizontal(parent, names, startColumn=0, startRow=0):
	buttons = []
	for i in range(0, len(names)):
		buttons.append(ttk.Button(parent, text=names[i], width=20))
		buttons[i].grid(column=i+startColumn, row=0+startRow)
	return buttons

def addAccountButton(parent, name, account, contentFrame, col=0):
	# print(account.attributes['name'])
	# print(account.schedules)
	button = ttk.Button(parent, text=name, width=20)
	button.grid(column=col, row=1)
	button.bind('<ButtonPress-1>', lambda e: displaySchedules(contentFrame, account))

def addAccountButtons(parent, names, accounts, contentFrame):
	for i in range(len(names)):
		addAccountButton(parent, names[i], accounts[i], contentFrame, i)

def createScheduleLabel(f, schedule):
	values = schedule.attributes
	names = list(values.keys())
	names.pop()
	widths = [15, 25, 25, 20, 10]
	sVars = [StringVar() for x in names]
	
	c = {'Credit': "light green", 'Debit': 'light pink'}
	c = c[schedule.attributes['paymentType']]
	for i in range(len(names)):
		sVars[i].set(values[names[i]])
		sVar = sVars[i].get()
		anchor = 'w'
		if names[i] == 'amount':
			anchor = 'e'
			sVar = locale.currency(float(sVar), grouping=True)
		l = ttk.Label(f, text=sVar, background=c, width=widths[i], borderwidth=1, relief='solid', anchor=anchor, padding=(5, 0, 5, 0))
		l.grid(column=i, row=0)
		l.bind('<Double-ButtonPress-1>', lambda e: ScheduleEditor(f, sVars, schedule))

def createHeadingLabels(f, names, widths):
	s = ttk.Style()
	s.configure('schedule.TFrame', background="dark gray")
	names.pop()
	for i in range(len(names)):
		l = ttk.Label(f, text=names[i].capitalize(), width=widths[i], borderwidth=1, relief='solid', anchor='center', padding=(5, 0, 5, 0))
		l.grid(column=i, row=0)


def displaySchedules(parent, account):
	for item in parent.winfo_children():
		item.destroy()
	scheduleHeadings = ["name", "payee", "amount", "frequency", "date", "paymentType"]
	scheduleWidths = [15, 25, 25, 20, 10]
	newScheduleButton = ttk.Button(parent, text='New Schedule', command=lambda: ScheduleMaker(account))
	newScheduleButton.grid(column=0, row=0, sticky='w')
	headingRow = createFrame(parent, 0, 1, 0)
	heading = createHeadingLabels(headingRow, scheduleHeadings, scheduleWidths)
	labelFrames = [createFrame(parent, 0, i+2, 0) for i in range(len(account.schedules))]
	for i in range(len(labelFrames)):
		createScheduleLabel(labelFrames[i], account.schedules[i])
