# -*- coding: utf-8 -*-
#BeautifulSoup

import requests
from bs4 import BeautifulSoup

#requestsでYahooジャパンのホームページの情報を取得
r = requests.get('https://www.yahoo.co.jp/')

#BeautifulSoupに取得した情報を渡す
soup = BeautifulSoup(r.text, 'html.parser')
#HTMLのクラスを利用して、タイトルのHTMLを取得
yahoo_news_titles = soup.select('._3cl937Zpn1ce8mDKd5kp7u')
#タイトルのHTMLから文字だけを抽出
for title in yahoo_news_titles:
    print(title.string)
