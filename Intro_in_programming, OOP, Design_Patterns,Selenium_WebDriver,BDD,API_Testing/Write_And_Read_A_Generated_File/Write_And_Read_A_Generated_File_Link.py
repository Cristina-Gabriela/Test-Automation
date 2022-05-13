doc = open("LINK_DOC.txt", 'w')
message_LINK_DOC = "https://goo.gl/maps/h8Bpzq5r6SDvC75e8"
doc.write(message_LINK_DOC)
doc.close()

doc = open("LINK_DOC.txt", 'r')
# doc.read(message_LINK_DOC)
# doc.close()
print(doc.read())
