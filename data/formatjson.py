import json

def getUserConfig(fileName):
	with open(fileName) as f:
	    return json.load(f)

def saveUserConfig(fileName, data):
	with open(fileName,'w') as f:
	    json.dump(data, f, indent=4)

file = "sysConfig.json"
data = getUserConfig(file)
saveUserConfig(file, data)