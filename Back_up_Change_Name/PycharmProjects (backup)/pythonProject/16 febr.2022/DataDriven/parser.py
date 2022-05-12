import json   # o structura a unui fisier si pot modela date in mai multe feluri.-- lista , excel...
import pathlib
import xmltodict as xmltodict
import xlrd

import pandas as pd
import numpy as np


def read_input_data(test_file):
    json_file = open(test_file)
    return json.load(json_file)  #dintr-un text care are forma de json, devine un incarca un dictionar


if __name__ == '__main__':
    test_data = read_input_data(
        "/home/cristina/PycharmProjects/pythonProject/16 febr.2022/DataDriven/TestData/Adresses.json")
    print(test_data)

    parent_location = pathlib.Path(__file__).parent.resolve()
    print(parent_location)
    current_file_location = pathlib.Path(__file__).resolve()
    print(current_file_location)
    # xml_file_name = "crypto.xml"
    # xml_file_location = f"{str(parent_location)}/{xml_file_name}"
    # print(xml_file_location)
    # xml_file = open(xml_file_location)
    # xml_file_content = xml_file.read()
    # print(xml_file_content)
    # dictionary_xml = xmltodict.parse(xml_file_content)
    # print(dictionary_xml)
    # current_txt_location = pathlib.Path(__file__).resolve()
    # print(current_txt_location)

    # txt_file_name = "Text.txt"
    # txt_file_location = f"{str(parent_location)}/{txt_file_name}"
    # print(txt_file_location)
    # txt_file_open = open(txt_file_location)
    # print(txt_file_open)
    # txt_file_read = txt_file_open.read()
    # print(txt_file_read)
    # txt_file = read_input_data("/home/cristina/PycharmProjects/pythonProject/16 febr.2022/DataDriven/Text.txt")
    # print(txt_file)

    # excel_file = pd.DataFrame(np.array([[10, 10, 20], [5, 5, 10], [6, 5, 10]]), columns=['X', 'Y', 'D'])
    # print(excel_file)
    #
    # sheet_name = "My_excel"

    # excel_file_name = "Ex. 2022.ods"
    # excel_parent_location = {"/home/cristina/Desktop"}
    # excel_file_location_address = f"{str(excel_parent_location)}/{excel_file_name}"
    # excel_file_open = xlrd.open_workbook(excel_parent_location)
    # sheet = excel_file_open.sheet_by_index(0)
    # print(sheet.cell_value(0))
    # excel_content = "Floare de primavara\tAbc\nGhiocel\tOrhidee"
    # excel_open = open("/home/cristina/Desktop/floare.xlsx", 'w')
    #
    # excel_open.write(excel_content)
    # excel_open.close()
    # excel_read = open("/home/cristina/Desktop/floare.xlsx")
    # excel_content = excel_read.read()
    # print(excel_content)



















# 1 Compunere Path # locatia (os.) Si acel path sa il concatenam  dinamic, OS...
# 2 Creare de fisiere, xml, excel, text- si sa le citesti pe toate.

#  text .txt
#  text .xsls
# creezi un excel :https://www.codegrepper.com/code-examples/python/create+an+excel+file+in+python
# il  pui intr-un string  open
# scrii stringul intr-un fisier  write
# citesti fisierul   read

#
# json_string = '''
# {
#     "student": [
#         {
#             "id": 10,
#             "buget": 0
#         },
#         {
#             "id": 10,
#             "buget": 2558852854
#         }
#     ]
# }
# '''
#
# #
# # created_instance = json.loads(json_string)
# # print(created_instance["student"])
