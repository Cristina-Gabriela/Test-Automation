import json

import requests

url = "http://httpbin.org/delete"

payload = "{\n    \"name\": \"Maria\",\n    \"age\": \"31\",\n    \"lastname\": \"chbdjabo\",\n    \"email\": \"nume.dcbsihcfbd@gmail.com\"\n}"
headers = {
    'Content-Type': 'text/plain'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)

x = response.json()
y = json.dumps(x)

with open("scratch_7.json", "w") as outfile:
    outfile.write(y)



