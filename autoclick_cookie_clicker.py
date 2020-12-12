from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re

PATH = 'C:\\Program Files\\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('https://orteil.dashnet.org/cookieclicker/')
print(driver.title)
articlee = driver.find_element_by_id("bigCookie")
time.sleep(5)

for i in range(0, 1000000, 1):
    articlee.click()

    product = driver.find_element_by_id("cookies")
    prop = product.text
    cookie = prop.split()

    pointer = driver.find_element_by_id("productPrice0")
    pointerplus = pointer.text

    product0 = driver.find_element_by_id("product0")
    if int(cookie[0]) > int(pointerplus):
        product0.click()

driver.quit()
