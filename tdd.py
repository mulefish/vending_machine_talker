import requests

url = "http://localhost:9092/avend?action=add&code=v2"
headers = {
    "User-Agent": "MyClient/1.0",
    "Content-Type": "application/json"
}
params = {
    "param1": "value1",
    "param2": "value2"
}

response = requests.get(url, headers=headers, params=params)