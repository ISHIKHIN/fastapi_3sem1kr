import requests

response = requests.post("http://localhost:8000/calculate", params={"num1": 5, "num2": 10})
print(response.json())

data = {"name": "Vika", "age": 20}
response = requests.post("http://localhost:8000/user", json=data)
print(response.json())

data = {"name": "Ivan", "message": "123324342342"}
response = requests.post("http://localhost:8000/feedback", json=data)
print(response.json())

data = {"name": "Ivan", "message": "Кринж рофл ужас кек уоу"}
response = requests.post("http://localhost:8000/feedback", json=data)
print(response.json())