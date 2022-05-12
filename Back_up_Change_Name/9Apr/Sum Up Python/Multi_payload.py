import requests
import json

url = "http://httpbin.org/get"

payload = json.dumps({
    "name_1": "Maria",
    "age_1": "31",
    "lastname_1": "chbdjabo",
    "email_1": "nume.abc@gmail.com",
    "name_2": "Ion",
    "age_2": "31",
    "lastname_2": "ccsfsfdo",
    "email_2": "fddf.fdfddvcd@gmail.com",
    "name_3": "Ion",
    "age_3": "31",
    "lastname_3": "ccsfsfdo",
    "email_3": "fddf.fdfddvcd@gmail.com"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)

x = response.json()
y = json.dumps(x)

with open("X.json", "w") as outfile:
    outfile.write(y)