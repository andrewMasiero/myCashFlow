import business
import json

def getSysConfig():
	with open("data/sysConfig.json") as f:
	    return json.load(f)	

def getUserConfig(fileName):
	with open("data/userConfig.json") as f:
	    return json.load(f)

def saveUserConfig(fileName, data):
	fileName = 'data/' + fileName + '.json'
	with open(fileName,'w') as f:
	    json.dump(data, f, indent=4)

def convertAccountToJson(account):
	j = {}
	j['attributes'] = dict(account.attributes)
	print('print schedules', account.schedules)
	j['schedules'] = [{"attributes":dict(x.attributes)} for x in account.schedules]
	return j

def save(fileName, userData):
	data = {}
	data['Main Account'] = convertAccountToJson(userData['Main Account'])
	data['Sub Accounts'] = [convertAccountToJson(a) for a in userData['Sub Accounts']]
	saveUserConfig(fileName, data)

def convertAccountToObject(account):
	schedules = [convertScheduleToObject(s) for s in account['schedules']]
	a = business.Account(account["attributes"])
	for s in schedules:
		a.addSchedule(s)
	return a

def convertScheduleToObject(schedule):
	s = business.Schedule(schedule["attributes"])
	return s

def loadUserData(file):
	userData = getUserConfig(file)
	objects = {'Main Account':{},
		"Sub Accounts":[convertAccountToObject(x) for x in userData['Sub Accounts']]}
	objects['Main Account'] = convertAccountToObject(userData['Main Account'])
	return objects
	