import requests as r
import json
import logging as l
import settings as s
payload = ''

def buildHeader():
	return{
		'Accept': "application/json",
    	'Content-Type': "application/json",
    	'Authorization': 'SSWS ' + s.APITOKEN,
    	'Host': s.HOST
		}

def removeAssignment(appId, userId):
	url = f"https://{s.HOST}/api/v1/apps/{appId}/users/{userId}"
	l.debug(url)
	headers = buildHeader()
	result = r.request("DELETE", url, data=payload, headers=headers)
	if result.status_code != 200:
		if result.status_code == 204:
			l.debug(f"User unassigned from app, user ID: {userId}")
			return True
		else:
			l.error(f"Unable to remove app assignment for user with ID: {userId}")
			return False
	response = json.loads(result.text)
	l.debug(f"User update: {userId} - Status: {response['status']}")
	return True

def getAssignments(appId):
	url = f"https://{s.HOST}/api/v1/apps/{appId}/users"
	l.debug(url)
	headers = buildHeader()
	result = r.request("GET", url, headers=headers)
	print(result)
	print(result.status_code)
	print(headers)
	if result.status_code != 200:
		l.error(f"Unable to retrieve users")
		return False
	response = json.loads(result.text)
	for user in response:
		if 'USER' in user['scope']:
			print(f"Object with scope USER found, User with ID: " + user['id'])
			removeAssignment(appId,user['id'])

def main():
	l.info('-- Start')
	getAssignments(s.APPID)

if __name__ == '__main__':
	main()