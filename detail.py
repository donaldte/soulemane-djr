import requests 

endpoint = "http://localhost:8000/api/crud/3/"

response = requests.get(endpoint)

print(response.text)

print(response.status_code)