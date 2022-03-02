# -*- coding: utf-8 -*-

import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys

#ブラウザの立ち上がる
browser = webdriver.Chrome()
#google newsを開く
browser.get('https://google.com')
#タグの名前で検索窓要素を取得
search = browser.find_element_by_tag_name('input')
search.send_keys('大阪 コロナ感染者数')
#エンターキーを押す
search.send_keys(Keys.ENTER)

news = browser.find_element_by_class_name('LC20lb') #HTMLオブジェクトを取得
news.click() #クリック
time.sleep(10)
