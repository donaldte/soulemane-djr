import requests 

endpoint = "http://localhost:8000/api/crud/4/"
data = {
    "name": "Product 4 update partial",
}
response = requests.patch(endpoint, data=data)

print(response.json())

print(response.status_code)