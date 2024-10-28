import requests 
from getpass import getpass
endpoint = "http://localhost:8000/api/token/"
username = input("Enter username: ")
password = getpass("Enter password: ")
response = requests.post(endpoint, json={'username': username, 'password': password})

status_code = response.status_code
endpoint = 'http://localhost:8000/api/mixins/'
data = {
        'name': 'New Product 100',
        'description': 'New Product Description',
        'price': 1000.00,
        'email': 'donald@gmail.com'
    }
if status_code == 200:
    print(response.json())
    token = response.json()['access']
    print('Token:', token)
    headers = {
        'Authorization': f'Bearer {token}' #{'Bearer' {tokent}}
    }
    
    response = requests.post(endpoint, json=data,  headers=headers)
    
    print(response.json())

else:
    response = requests.post(endpoint, json=data)
    print(response.text)      