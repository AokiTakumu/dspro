from bs4 import BeautifulSoup
import requests
import time

# アクセスしたいWebサイトのURL
url = 'https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=43&block_no=47626&year=2023&month=12&day=&view=a2'

# Webサーバにリクエストを出す．レスポンスを変数に格納しておく
r = requests.get(url)

# 1秒待機
time.sleep(1)

html_soup = BeautifulSoup(r.content, "html.parser")

# tdタグをすべて取得
td_tags = html_soup.find_all('td', class_='data_0_0')

# 取得したtdタグの内容を出力
for td_tag in td_tags:
    print(td_tag.text)
