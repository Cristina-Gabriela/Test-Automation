import json

import requests

url = "http://httpbin.org/delete"

payload = json.dumps({
           "name": "Maria",
           "age": "31",
           "lastname": "chbdjabo",
           "email": "nume.dcbsihcfbd@gmail.com"
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)


print(response.status_code)


