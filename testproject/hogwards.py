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

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html")

passenger_field = driver.find_element_by_id("passenger")
passenger = "Harry Potter"
passenger_field.send_keys(passenger)

# date input filling
departure_date = driver.find_element_by_id('departure-date')
date_to_set = datetime(2021, 7, 28)
departure_date.send_keys(date_to_set.strftime('%m'))
departure_date.send_keys(date_to_set.strftime('%d'))
departure_date.send_keys(date_to_set.strftime('%Y'))


# time input filling
departure_time = driver.find_element_by_id('departure-time')
date_to_set = datetime(2021, 7, 28, 12, 25)
departure_time.send_keys(date_to_set.strftime('%I:%M'))
departure_time.send_keys(date_to_set.strftime('%p'))

# ticket creation activation
issue_button = driver.find_element_by_id("issue-ticket")
issue_button.click()


# asserts validations
assert driver.find_element_by_id("passenger-name").text == passenger.upper()
assert driver.find_element_by_id("departure-date-text").text == "2021-07-28"
assert driver.find_element_by_id("departure-time-text").text == "12:25PM"

# nincs időm függvénybe szervezni
