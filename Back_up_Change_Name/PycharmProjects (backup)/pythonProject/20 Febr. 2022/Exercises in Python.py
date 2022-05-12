# 1. Variabila = Open : In primul rand stabilesti locatia in calculator pentru fisier si o scrii.(ex. Desktop)
# 2. Variabila = Write: Apoi scrii continutul in fisierul pe care l-ai deschis cu ajutorul functiei write.
# 3. (Continutul scris poate fi prestabilit inainte printr-o variabila). Aceasta va fi scrisa in ().
# 4. open.close(): Odata ce a fost stabilita locatia, s-a deschis fisierul si s-a scris in interior textul (chiar si in format excel).Se inchide prin functia close.
# 5. Variabila = Open(locatie): Se declara o noua variabila de deschidere a continutului.Se foloseste  locatia -parinte (default): open(locatia)
# 6. Variabila = Read:  Se declara aceeasi variabila care contine textul, care va avea ca scop citirea continutului recent deschis si ulterior scris : Variabila open.read()
# 7. Print(variabila initala care contine continutul text.  )
#
# a = "<crypto coin = 'Money'>\n<investor>Afdkjd jnjkdsn</investor>\n<investor>Afjcdfj fvjdkg</investor>\n<investor>Dbhjbs fdjfhfd</investor>\n</crypto>"
# b = open("/home/cristina/Desktop/Crypto.xml", 'w')
# b.write(a)
# b.close()
#
# c = open("/home/cristina/Desktop/Crypto.xml")
# a = c.read()
# print(a)
# sau print(c.read())

excel_content_1 = "Spring\tFlowers\tNumbers\nOK\thyacinth\t1000002"
excel_open_1 = open("/home/cristina/Desktop/Spring.xlsx", 'w')
excel_open_1.write(excel_content_1)
excel_open_1.close()
excel_read_1 = open("/home/cristina/Desktop/Spring.xlsx")
excel_content_1 = excel_read_1.read()
print(excel_content_1)

txt_content_2 = "This season in the year, the Spring.\n Spring (2019 film), a computer-animated short film created by the Blender Institute"
txt_open_location_2 = open("/home/cristina/Desktop/Spring.txt", 'w')
txt_open_location_2.write(txt_content_2)
txt_open_location_2.close()
txt_read_location_2 = open("/home/cristina/Desktop/Spring.txt")
txt_content_2 = txt_read_location_2.read()
print(txt_content_2)
print("")

Msg_xml = "<crypto coin = 'Money'>\n<investor>Afdkjd jnjkdsn</investor>\n<investor>Afjcdfj fvjdkg</investor>\n<investor>Dbhjbs fdjfhfd</investor>\n</crypto>"
Send_xml = open("/home/cristina/Desktop/Crypto.xml", 'w')
Send_xml.write(Msg_xml)
Send_xml.close()

Receive_xml = open("/home/cristina/Desktop/Crypto.xml")
Msg_xml = Receive_xml.read()
print(Msg_xml)


sending_message = "Did you hear about the news ?"
road_map_message = open("/home/cristina/Desktop/Conversation.pdf",'w')
road_map_message.write(sending_message)
road_map_message.close()

receiving_message = open("/home/cristina/Desktop/Conversation.pdf")   # sau alta pt o anumita persoana
sending_message = receiving_message.read()
print(sending_message)

response_message = "Yes, of corse. The news are very good."
road_map_message_r = open("/home/cristina/Desktop/Response.pdf",'w')
road_map_message_r.write(response_message)
road_map_message_r.close()

response_message_read = open("/home/cristina/Desktop/Response.pdf")
response_message= response_message_read.read()
print(response_message)


facebook_msg = "What do you think that is the best job for 2022 ?"
person_1 = open("/home/cristina/PycharmProjects/pythonProject/20 Febr. 2022/Facebook Conversation.py", 'w')
person_1.write(facebook_msg)
person_1.close()

person_2 = open("/home/cristina/PycharmProjects/pythonProject/20 Febr. 2022/Facebook Conversation.py")
facebook_msg = person_2.read()
print(facebook_msg)



facebook_response = "I think that Automation is. And all the jobs related to IT (Telecommunication, also). Did you think the same?"
person_B = open("/home/cristina/PycharmProjects/pythonProject/20 Febr. 2022/Facebook_response.py", 'w')
person_B.write(facebook_response)
person_B.close()

person_A = open("/home/cristina/PycharmProjects/pythonProject/20 Febr. 2022/Facebook_response.py")
facebook_response = person_A.read()
print(facebook_response)




import pathlib
parent_location = pathlib.Path(__file__).parent.resolve()
print(parent_location)
child_location = pathlib.Path(__file__).resolve()
print(child_location)
# Facebook_response = pathlib.Path(__file__).Facebook_response.py.resolve()
# print(Facebook_response)
