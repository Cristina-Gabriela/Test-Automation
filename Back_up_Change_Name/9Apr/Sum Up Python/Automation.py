import requests
import json

url = "http://httpbin.org/get"

payload = "{\n    \"name\": \"Maria\",\n    \"age\": \"31\",\n    \"lastname\": \"chbdjabo\",\n    \"email\": \"nume.abc@gmail.com\"\n    \"name\": \"Ioan\",\n    \"age\": \"31\",\n    \"lastname\": \"chbdjabo\",\n    \"email\": \"nume.bvc@gmail.com\"\n    \"name\": \"X\",\n    \"age\": \"31\",\n    \"lastname\": \"chbdjabo\",\n    \"email\": \"nume.dsfbd@gmail.com\"\n    \"name\": \"Y\",\n    \"age\": \"31\",\n    \"lastname\": \"chbdjabo\",\n    \"email\": \"nume.wrtd@gmail.com\"\n}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.json())
print(response.status_code)

x = response.json()
json.dumps(x)
print(x)

Abc = json.dumps(x)


with open("scratch_10.json", "w") as outfile:
    outfile.write(Abc)



import requests

url = "http://httpbin.org/get"

payload = "{\n    \"name\": \"Maria\",\n    \"age\": \"31\",\n    \"lastname\": \"chbdjabo\",\n    \"email\": \"nume.abc@gmail.com\"\n}"
headers = {
  'Content-Type': 'text/html'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)










