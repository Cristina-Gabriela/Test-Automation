import requests
import json

http_bin_url = "http://httpbin.org?my_parameter=1&my_parameter=2&my_name=xyz"


def make_request(request_body, url, input_headers, method="GET"):
    print(request_body)
    name_field = json.loads(request_body)["name"]
    assert name_field == "Cristina"

    a = requests.request(method, url, data=request_body, headers=input_headers)
    print(a)


payload = json.dumps({
    "name": "Cristina",
    "age": "31",
    "lastname": "chbdjabo",
    "email": "nume.dcbsihcfbd@gmail.com"
})
headers = {
    'Content-Type': 'application/json'
}
# CLASA     # Metoda a clasei-- functie
make_request(payload, url="http://google.com", input_headers=headers)
payload_2 = json.dumps({
    "life": "105"
})
make_request(request_body=payload_2, url=http_bin_url, input_headers="")
make_request("", "http://google.com", "")

    # assert "name" in make_request()



make_request(payload, url="http://google.com", input_headers=headers, method="POST")
payload_2 = json.dumps({
    "life": "105"
})
make_request(request_body=payload_2, url=http_bin_url, input_headers="",method="DELETE" )
make_request("", "http://google.com", "")

    # assert "name" in make_request()



