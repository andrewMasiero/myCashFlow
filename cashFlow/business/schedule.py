from tkinter import *
from tkinter import ttk

class Schedule:
	def __init__(self, schedule):
		self.attributes = {}
		self.attributes['name'] = schedule['name']
		self.attributes['payee'] = schedule['payee']
		self.attributes['amount'] = schedule['amount']
		self.attributes['frequency'] = schedule['frequency']
		self.attributes['date'] = schedule['date']
		self.attributes['paymentType'] = schedule['paymentType']		
	
	def setAttribute(self, k, v):
		self.attributes[k] = v
	
	def getAttribute(self, k):
		return self.attributes[k]

	def printAttributes(self):
		print('Schedule Name: ', self.attributes['name'])
		print('Payee: ', self.attributes['payee'])
		print('Amount: ', self.attributes['amount'])
		print('Frequency: ', self.attributes['frequency'])
		print('Next due date: ', self.attributes['date'])
		print('Payment type: ', self.attributes['paymentType'])
		print()
