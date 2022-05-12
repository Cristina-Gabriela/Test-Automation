# import json
#
# def ceva(text):
#     file = open(text)
#     return json.load(file)
#
# if __name__ == '__main__':
#     a = ceva("/home/cristina/PycharmProjects/pythonProject/18 Ian 2022/Learn Py_json/Learn_Json.py")
#     print(a)


import json

def ceva(text):
    file = open(text)
    return json.load(file)

if __name__ == '__main__':
    a = ceva("file:///home/cristina/Desktop/1.xml")
    print(a)