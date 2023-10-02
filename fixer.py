import json

with open('users.json', 'r') as file:
	userdict = json.load(file)

for key in userdict:
	userdict[key]['notif'] = 0

with open('users.json', 'w') as file:
	json.dump(userdict, file)
