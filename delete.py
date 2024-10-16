import requests 

endpoint = "http://localhost:8000/api/crud/4/"
data = {
    "name": "Product 4 update",
    "content": "Product 10 content",
    "price": 100.00
}
response = requests.delete(endpoint)

print(response.json())

print(response.status_code)