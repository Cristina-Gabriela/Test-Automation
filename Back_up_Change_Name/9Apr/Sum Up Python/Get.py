# import requests
#
# url = "http://httpbin.org?my_parameter=1&my_parameter=2&my_name=xyz"
#
# payload = {
#
# }
# headers = {
#
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.status_code)
#
# if response.status_code == 200:
#     print('test passed')
#     res = response.json()
#     print(res)
#
#
#
# # print(response.text)
# print(response.status_code)
# print(type(response.status_code))


# import requests
# import json
#
# url = "http://httpbin.org?my_parameter=1&my_parameter=2&my_name=xyz"
#
# payload = json.dumps({
#   "name": "Maria",
#   "age": "31",
#   "lastname": "chbdjabo",
#   "email": "nume.dcbsihcfbd@gmail.com"
# })
# headers = {
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# # print(response.text)
# print(response.status_code)
#
#
# if response.status_code == 200:
#     print("Test passed")
#     res = response.json()
# print(res)


# print(response.text)
# print(response.request)
# print(response.status_code)
# print(type(response.status_code))


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
