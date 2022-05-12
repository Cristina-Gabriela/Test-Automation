file = open("DOC.txt", "w")
Story = ["This is a good day ! \n", "This is a good day ! \n"]
Message = "Good morning !"

file.write(Message)

# # file.write(Story)
#
# file.close()
# file = open("DOC.txt", 'r')
# print(file.read())
# file.close()

variable = open("Incognito.py", "w")
message = "I would like to be a professional Software developer."
variable.write(message)
variable.close()


variable = open("Incognito.py", "r")
print(variable.read())
# print(variable.write())

