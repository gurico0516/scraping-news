# -*- coding: utf-8 -*-

import time
from selenium import webdriver
import chromedriver_binary

# 1) Initialize Chrome
# DRIVER_PATH is dependent on your environment.

driver = webdriver.Chrome()

# 2) Open the Google page
driver.get('https://www.google.com')

#### Fig.1

# 3) Wait until the page
time.sleep(3)

# 4) Get an object of the search box
q = driver.find_element_by_name('q')

# 5) Send the key to the search box
q.send_keys('ニュース')

#### Fig.2

# 6) submit the form
q.submit()

# 7) Wait in 10 seconds
time.sleep(10)

#### Fig.3

# 8) Finalize the driver
driver.quit()
