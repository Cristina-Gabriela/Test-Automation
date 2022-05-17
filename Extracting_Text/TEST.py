from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("https://en.wikipedia.org/wiki/Python_(programming_language)")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "html.parser")

html_text = soup.get_text()

f = open("Extracting_Python_text", "w")

for line in html_text:
    f.write(line)

f.close()

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("https://en.wikipedia.org/wiki/Test_automation")
OPEN_link = urlopen(req)
soup = BeautifulSoup(OPEN_link, "html.parser")
Recieve_Text = soup.get_text()
Folder_Text = open('Extracting_Text_Test_Automation', "w")

for i in Recieve_Text:
    Folder_Text.write(i)

Folder_Text.close()

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("https://en.wikipedia.org/wiki/Diamond")
OPEN = urlopen(req)
soup = BeautifulSoup(OPEN, "html.parser")
Recieve_text = soup.get_text()
Folder_text = open("Extracting_Text_Diamant", "w")

for character in Recieve_text:
    Folder_text.write(character)

Folder_text.close()

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

REQ = Request("https://saucelabs.com/")
OPEN = urlopen(REQ)
soup = BeautifulSoup(OPEN, "html.parser")
Recieve_text = soup.get_text()
Folder_text = open("Extracting_Text_Site_Saucelabs", "w")
for i in Recieve_text:
    Folder_text.write(i)

Folder_text.close()

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

REQ = Request("https://saucelabs.com/security")
OPEN = urlopen(REQ)
soup = BeautifulSoup(OPEN, "html.parser")
Recieve_text = soup.get_text()
Folder_text = open("Extracting_Text_Site_Saucelabs_Security", "w")
for i in Recieve_text:
    Folder_text.write(i)

Folder_text.close()

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("https://www.geeksforgeeks.org/extract-title-from-a-webpage-using-python/")
OPEN = urlopen(req)
soup = BeautifulSoup(OPEN, "html.parser")
Recieve_text = soup.get_text()
Folder_text = open("Extracting_Text_Site_Geeksforgeeks", "w")

for i in Recieve_text:
    Folder_text.write(i)

Folder_text.close()



