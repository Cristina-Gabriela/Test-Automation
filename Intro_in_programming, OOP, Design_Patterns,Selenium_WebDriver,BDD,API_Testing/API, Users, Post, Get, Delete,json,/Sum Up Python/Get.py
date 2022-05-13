
import requests
import json

url = "http://httpbin.org/get"

payload = json.dumps({
    "name": "Maria",
    "age": "31",
    "lastname": "chbdjabo",
    "email": "nume.dcbsihcfbd@gmail.com"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)
x = response.json()

x_string = json.dumps(x)

with open('scratch_5.json', "w") as outfile:
    outfile.write(x_string)
with open('x.json', "w") as outfile:
    outfile.write(x_string)




