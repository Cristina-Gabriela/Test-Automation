import requests
import json

url = "http://httpbin.org/post"

payload = "{\n    \"name\":\"Cris\"\n    \"age\":\"31\"\n    \"email\":\"innovation@gmail.com\"\n}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.status_code)
print(type(response.status_code))

if response.status_code == 200:
    print("Test Passed")
    x = response.json()
    print(x)

# print(x["json"]["age"])
# print(response.text)

