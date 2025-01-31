from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html")

go_button = driver.find_element_by_class_name("btn-go")
go_button.click()

# TC01: üres kitöltés helyessége
assert driver.find_element_by_id("disclaimer").text == "Enter the property value before clicking Go button."
assert driver.find_element_by_id("tax").get_attribute("value") == ""


# TC02: helyes kitöltés helyes kitöltése
estimate_field = driver.find_element_by_id("price")
# time.sleep(2)
estimate_field.send_keys("33333")
go_button.click()
assert driver.find_element_by_id("tax").get_attribute("value") == "16.665"

# test failed

#12 pont / a teszt a "33333" input adattal valóban nem a 16.665 értéket eredményezi, azaz valóban bukik a teszt,
# de nálad hiányzik a kódból az érték rész: driver.find_element_by_id("tax").get_attribute("value") ezért hibás az assert,
# illetve az első assert-nél is a text-et vizsgáltad a value helyett.