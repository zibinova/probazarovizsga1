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
assert driver.find_element_by_id("tax").text == ""


# TC02: helyes kitöltés helyes kitöltése
estimate_field = driver.find_element_by_id("price")
# time.sleep(2)
estimate_field.send_keys("33333")
go_button.click()
assert driver.find_element_by_id("tax") == "16.665"

# test failed