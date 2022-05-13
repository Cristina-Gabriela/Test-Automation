import requests

url = "http://httpbin.org?my_parameter= 250&my_parameter=125&my_age=31"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.status_code)



