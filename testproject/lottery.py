from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html")

# TC01: lotto huzas elott nem ismertek a szamok
# nem szabad, hogy akár csak egy szám is megjelenjen mielőtt az első alkalommal a "Generate" feliratú gombra kattintunk

draw_button = driver.find_element_by_id("draw-number")
reset_button = driver.find_element_by_id("reset-numbers")
balls = driver.find_elements_by_class_name("balls")
assert len(balls) == 0

# TC02: lottohuzás működik
# Nyomjuk meg hatszor a "Generate" feliratú gombot
# Ellenőrizzük, hogy pontosan 6db szám jelenik meg a képernyőn
# Olvassuk ki a számokat és ellenőrizzük, hogy mind 1 és 59 között vannak

for _ in range(6):
    draw_button.click()

time.sleep(2)
# assert len(balls) == 6

ball1 = driver.find_element_by_xpath("//*[@id='container']/div[1]").text
ball2 = driver.find_element_by_xpath("//*[@id='container']/div[2]").text
ball3 = driver.find_element_by_xpath("//*[@id='container']/div[3]").text
ball4 = driver.find_element_by_xpath("//*[@id='container']/div[4]").text
ball5 = driver.find_element_by_xpath("//*[@id='container']/div[5]").text
ball6 = driver.find_element_by_xpath("//*[@id='container']/div[6]").text
time.sleep(2)
number_list = int(ball1),  int(ball2),  int(ball3),  int(ball4), int(ball5), int(ball6)
print(len(number_list))

for number in number_list:
    assert 1 <= number <= 59

# TC03: lottohúzás befejeződött
# Nyomjuk meg 7x is a "Generate" feliratú gombot
# Ellenőrizzük, hogy pontosan nem jelent meg hetedik szám
# Nyomjuk meg a "Reset" feliratú gombot
# nem szabad, hogy akár csak egy szám is megjelenjen miután a "Reset" gombot megnyomtuk

draw_button.click()
assert len(number_list) == 6

reset_button.click()
assert len(balls) == 0
