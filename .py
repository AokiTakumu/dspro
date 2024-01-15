from bs4 import BeautifulSoup
import requests
import time

# アクセスしたいWebサイトのURL
url = 'https://www.data.jma.go.jp/stats/etrn/view/monthly_s1.php?prec_no=43&block_no=47626&year=2023&month=&day=&view='

# Webサーバにリクエストを出す．レスポンスを変数に格納しておく
r = requests.get(url)

# 1秒待機
time.sleep(1)