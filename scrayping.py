import requests
from bs4 import BeautifulSoup
import time
import sqlite3

# スクレイピング対象のURL
url = "https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=43&block_no=47626&year=2023&month=12&day=&view=a2"

# ページの取得
response = requests.get(url)

# サーバーへの負荷を軽減するために待機
time.sleep(1)

# ページのHTMLをBeautifulSoupで解析
soup = BeautifulSoup(response.text, 'html.parser')

# 平均気温の部分を特定
average_temperature_elements = [td for i, td in enumerate(soup.select('td.data_0_0')) if i % 18 == 9]  # 10番目、28番目、46番目...の要素

# 平均気温の値を取得 (数字以外の文字列は無視する)
average_temperatures = [float(element.text) for element in average_temperature_elements if element.text.replace('.', '').isdigit()]

# SQLiteデータベースに接続
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# テーブルが存在しない場合は作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS average_temperatures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature REAL
    )
''')

# 取得した平均気温をデータベースに挿入
for temperature in average_temperatures:
    cursor.execute('INSERT INTO average_temperatures (temperature) VALUES (?)', (temperature,))

# 変更をコミット
conn.commit()

# 接続を閉じる
conn.close()