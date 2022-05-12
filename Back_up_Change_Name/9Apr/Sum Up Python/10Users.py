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
    "name_3": "Felix",
    "age_3": "37",
    "lastname_3": "Dmnfdls",
    "email_3": "nkfdjnfkfd@gmail.com",
    "name_4": "Angela",
    "age_4": "40",
    "lastname_4": "fefdgtr",
    "email_4": "ngtrtmk@gmail.com",
    "name_5": "Sorin",
    "age_5": "27",
    "lastname_5": "cfjdbgdo",
    "email_5": "gtrfresgt@gmail.com",
    "name_6": "Evelina",
    "age_6": "22",
    "lastname_6": "bgrtgrttr",
    "email_6": "ftgrgtrd@gmail.com",
    "name_7": "Olivian",
    "age_7": "45",
    "lastname_7": "cfegtre",
    "email_7": "gtrgtryhj@gmail.com",
    "name_8": "Li",
    "age_8": "51",
    "lastname_8": "ctfegtr",
    "email_8": "tgretge@gmail.com",
    "name_9": "Lyi",
    "age_9": "33",
    "lastname_9": "vgrgtse",
    "email_9": "ftgretyehd@gmail.com",
    "name_10": "Mark",
    "age_10": "30",
    "lastname_10": "ergrfse",
    "email_10": "gtfrhdryhr@gmail.com"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)

# x = response.json()
# y = json.dumps(x)
#
# with open("scratch_11.json", "w") as outfile:
#     outfile.write(y)


def make_request(payload, url):

















