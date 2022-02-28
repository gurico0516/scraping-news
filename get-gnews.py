# -*- coding: utf-8 -*-
#Selenium

from selenium import webdriver
import chromedriver_binary

#ブラウザを立ち上げる
browser = webdriver.Chrome()
#google newsを開く
browser.get('https://news.google.com/topstories?tab=wn&hl=ja&gl=JP&ceid=JP:ja')
#クラスでトップ記事の見出しを取得
top = browser.find_elements_by_class_name('ipQwMb')

#タイトルを表示
for title in top:
    print(title.text)
