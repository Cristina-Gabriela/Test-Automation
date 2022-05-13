import requests
import json

url = "https://httpbin.org/post"

payload = json.dumps({
    "name":
        {
            "email2": "sfdefcdfd@gmail.com",
            "email3": "qedwdfsfc@gmail.com"
        },
    "age": "31",
    "lastname": "chbdjabo",
    "email": "nume.dcbsihcfbd@gmail.com"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)

response_dict = response.json()

print(response_dict)
print(response_dict["json"]["name"]["email2"])
print(response_dict["json"])
print(response_dict["json"]["name"])


if response.status_code == 200:
    print("test passed")























# response_string = json.dumps(response_dict)
#
# with open('scratch_4.json', 'w') as outfile:
#     outfile.write(response_string)















