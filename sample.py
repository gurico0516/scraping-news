# -*- coding: utf-8 -*-

import time
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()

driver.get('https://www.google.com')

time.sleep(3)

q = driver.find_element_by_name('q')

q.send_keys('大阪 コロナ感染者数')

q.submit()

time.sleep(10)

driver.quit()
