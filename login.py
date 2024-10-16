import requests 
from getpass import getpass
endpoint = "http://localhost:8000/api/login/"
username = input("Enter username: ")
password = getpass("Enter password: ")
response = requests.post(endpoint, json={'username': username, 'password': password})

token = response.json()['token']
endpoint = 'http://localhost:8000/api/mixins/'

if token:
    headers = {
        'Authorization': f'Token {token}' #{'Barear' {tokent}}
    }
    response = requests.get(endpoint, headers=headers)
    
    print(response.json())

else:
    print(response.text)      