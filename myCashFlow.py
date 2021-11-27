import datetime
import cfi
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from data.cashFlowConfig import sysConfig
import data
import business

file = "userConfig"
# sysConfig = data.getSysConfig()
userData = data.loadUserData(file)
accountNames = ['Main'] + [s.attributes['name'] for s in userData['Sub']]
accounts = [userData['Main']]
[accounts.append(x) for x in userData['Sub']]


# start drawing UI
root = cfi.createMainWindow()
style = ttk.Style()
style.configure('cf.TFrame', background="dark gray")
mainFrame = ttk.Frame(root, padding=20, relief='groove', style='cf.TFrame')
mainFrame.pack()

menuFrame = cfi.createFrame(mainFrame, 0, 0, 20)
contentFrame = cfi.createFrame(mainFrame, 0, 1, 20)

menuButtons = cfi.addButtonsHorizontal(menuFrame, sysConfig['mainMenuTitles'], 0, 0)
cfi.addAccountButtons(menuFrame, accountNames, accounts, contentFrame)
cfi.displaySchedules(contentFrame, accounts[0])

root.bind('<Escape>', lambda e: root.destroy())
root.bind('<Control-s>', lambda e: data.cfDataManager.save('test', userData))
root.mainloop()

# cal = DateEntry(contentFrame).grid()