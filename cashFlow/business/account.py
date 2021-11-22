class Account:
	def __init__(self, account):
		self.attributes = {}
		self.attributes['name'] = account['name']
		self.attributes['balance'] = account['balance']
		self.attributes['apr'] = account['apr']
		self.attributes['maxBalance'] = account['maxBalance']
		self.attributes['minBalance'] = account['minBalance']
		self.attributes['creditLimit'] = account['creditLimit']
		self.attributes['minPayment'] = account['minPayment']
		try:
			self.schedules = account['schedules']
		except:
			self.schedules = []
		
	def setAttribute(self, k, v):
		self.attribute[k] = v

	def getAttribute(self, k):
		return self.attribute[k]

	def addSchedule(self, x):
		self.schedules.append(x)

	def removeSchedule(self, x):
		self.schedules.remove(x)

	def getScheduleByName(self, name):
		for s in self.schedules:
			if s.name==name:
				return s 

	def getAllSchedules(self):
		return self.schedules

	def printAttributes(self):


		print('Account Name: ', self.attributes['name'])
		print('Balance: ', self.attributes['balance'])
		print('APR: ', self.attributes['apr'])
		print('Max Balance: ', self.attributes['maxBalance'])
		print('Min Balance: ', self.attributes['minBalance'])
		print('Credit Limit: ', self.attributes['creditLimit'])
		print('Minimum Payment: ', self.attributes['minPayment'])
		print()

	def sortSchedules():
		array = self.schedules
		n = len(array)
		for i in range(n):
			already_sorted = True
			for j in range(n - i - 1):
				if array[j].date > array[j + 1].date:
					array[j], array[j + 1] = array[j + 1], array[j]
					already_sorted = False
			if already_sorted:
				break
		return array