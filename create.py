import requests 

endpoint = "http://localhost:8000/api/crud/"
data = {
    "name": "P",
    "content": "Product 10 content",
    "price": 100.00
}
response = requests.post(endpoint, data=data)

print(response.text)

print(response.status_code)