# import self
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# def setUp(self):
#     self.driver = webdriver.Chrome(ChromeDriverManager().install())
#
#
# doc = open("LINK_DOC.txt", 'w')
#
# message_LINK_DOC = self.driver.find_element(By.CLASS_NAME, "vrsrZe")
#
# doc.write(message_LINK_DOC)
# doc.close()
#
# print(message_LINK_DOC.get_attribute('value'))
#
# doc = open("LINK_DOC.txt", 'r')
# # doc.read(message_LINK_DOC)
# # doc.close()
# print(doc.read())

doc = open("Test.py", "w")
message = "Hello"
doc.write(message)
doc.close()
doc = open("Test.py", "r")
doc.read(message)
doc.close()

print(doc.read)

























