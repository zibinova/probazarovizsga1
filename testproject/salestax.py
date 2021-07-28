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

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html")

subtotal_button = driver.find_element_by_id("subtotalBtn")
subtotal_field = driver.find_element_by_id("subtotal")
gtotal_button = driver.find_element_by_id("gtotalBtn")
gtotal_field = driver.find_element_by_id("gtotal")

# TC01: üres kitöltés helyessége,
# -"Subtotal" feliratú gomb megnyomásakor a salestax azonosítójú mező 0.00 értéket kell mutasson,
# -Calculate Order" gomb megyomására a gtotal mező 4.95 értéket kell mutasson

subtotal_button.click()
# print(driver.find_element_by_id("subtotal").get_attribute("value"))
assert subtotal_field.get_attribute("value") == "0.00"
gtotal_button.click()
assert gtotal_field.get_attribute("value") == "4.95"

# TC02: 6" x 6" Volkanik Ice kitöltés helyessége

# válasszuk ki a Product Item feliratú mezőből a 6" x 6" Volkanik Ice értéket
# a quantity feliratú mezőbe írjunk 1-et
# ellenőrizzük, hogy a "Subtotal" feliratú gomb megnyomásakor a salestax azonosítójú mező 4.95 értéket kell mutasson.
# illetve a "Calculate Order" gomb megyomására a gtotal mező 9.90 értéket kell mutasson

proditem_field = driver.find_element_by_xpath("//*[@id='Proditem']/option[2]")
proditem_field.click()
driver.find_element_by_id("quantity").send_keys("1")
subtotal_button.click()
assert subtotal_field.get_attribute("value") == "4.95"
gtotal_button.click()
assert gtotal_field.get_attribute("value") == "9.90"

# a salestax id-val rendelkező field nem mutat 4.95-ot, azt a subtotal adja, tehat a teszt bukik
assert driver.find_element_by_id("salestax").get_attribute("value") == "4.95"
