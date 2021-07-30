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

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html")

email_input_field = driver.find_element_by_xpath("//*[@id='section-timesheet']/div[1]/form/input[1]")
next_button = driver.find_element_by_xpath("//*[@id='buttons']/input")

# TC01: üres kitöltés helyessége
# ha nincs kitoltve az e-mail mező nem lehet megnyomni a "next" feliratú gombot

email_input_field.send_keys("")
assert not next_button.is_enabled()

# ha helytelen (formailag helytelen) e-mailcimmel probáljuk kitölteni a formot nem lehet megnyomni
# a "next" feliratú gombot

email_input_field.send_keys("testergamil.hu")
assert not next_button.is_enabled()

# TC02: helyes kitöltés helyes köszönet képernyő

# Clear button megnyomása
driver.find_element_by_xpath('//*[@id="buttons"]/button').click()
email_input_field.send_keys("test@bela.hu")

driver.find_element_by_xpath("//*[@id='section-timesheet']/div[1]/form/input[2]").send_keys("2")
driver.find_element_by_xpath("//*[@id='section-timesheet']/div[1]/form/input[3]").send_keys("0")
driver.find_element_by_xpath("//*[@id='section-timesheet']/div[1]/form/textarea").send_keys("working hard")
driver.find_element_by_xpath("//*[@id='dropDown']/option").click()
next_button.click()

time.sleep(3)
assert driver.find_element_by_xpath("//*[@id='section-thankyou']/div/p[2]/span[1]").text == "2"
assert driver.find_element_by_xpath("//*[@id='section-thankyou']/div/p[2]/span[2]").text == "0"

driver.close()
