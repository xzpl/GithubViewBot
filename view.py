import selenium.webdriver
from selenium.webdriver.chrome.options import Options
import time

user = "https://github.com/4b3j"

opti = Options()
opti.add_argument("--headless")
opti.add_argument("--disable-gpu")

views = 0

while True:
    brow = selenium.webdriver.Chrome(options=opti)

    brow.get(user)
    brow.close()
    views+=1
    print(f"View {views}")
