import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://api.pingdom.com/api/2.0/checks"
headers = {'App-Key' : 'YOUR APP KEY', 'Account-Email' : 'PINGDOM ACCOUNT EMAIL', 'Content-Type' : 'application/json'}
user = 'PINGDOM USER NAME'
password = 'PINGDOM USER PASSWORD'

def getCheckNamesAndIds():
	print('Getting list of Pingdom check names and Ids...' + '\n')
	response = requests.get(url, auth = HTTPBasicAuth(user, password), headers = headers)

	if(response.ok):
		json = response.json()
		checks = json['checks']
		
		for n in checks:
			print(n['name'] + ' : ' + str(n['id']))
	else:
		response.raise_for_status()

def pauseSingleCheck(input):
	check_url = url + '/' + input
	payload = {'paused':'true'}
	response = requests.put(check_url, auth = HTTPBasicAuth(user, password), headers = headers, params = payload)
	
	if(response.ok):
		print('Check Id ' + input + ' successfully paused.')
	else:
		response.raise_for_status()
	
def resumeSingleCheck(input):
	check_url = url + '/' + input
	payload = {'paused':'false'}
	response = requests.put(check_url, auth = HTTPBasicAuth(user, password), headers = headers, params = payload)
	
	if(response.ok):
		print('Check Id ' + input + ' successfully unpaused.')
	else:
		response.raise_for_status()
	

	
getCheckNamesAndIds()
check_id = input('Select check by Id:  ')

while True:
	action = input('Pause/unpause: ')
	if(action == 'pause'):
		pauseSingleCheck(check_id)
		break
	elif(action == 'unpause'):
		resumeSingleCheck(check_id)
		break
	else:
		print('Please enter "pause" or "unpause"')
		continue