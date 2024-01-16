import sqlite3

# 睡眠データ
sleep_data_list = [
    (3.5,),
    (4.0,),
    (4.0,),
    (4.0,),
    (2.2,),
    (4.0,),
    (4.0,),
    (2.7,),
    (4.0,),
    (3.2,),
    (4.0,),
    (0.3,),
    (3.7,),
    (4.0,),
    (2.4,),
    (4.0,),
    (4.0,),
    (4.0,),
    (4.0,),
    (4.0,),
    (0.0,),
    (2.2,),
    (4.0,),
    (4.0,),
    (1.5,),
    (4.0,),
    (2.8,),
    (3.7,),
    (2.7,),
    (1.7,),
    (4.0,)
]

# SQLiteデータベースに接続
conn = sqlite3.connect('sleep_data.db')
cursor = conn.cursor()

# テーブルが存在しない場合は作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sleep_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        duration REAL
    )
''')

# 複数のデータを一括で挿入
cursor.executemany('INSERT INTO sleep_data (duration) VALUES (?)', sleep_data_list)

# 変更をコミット
conn.commit()

# 接続を閉じる
conn.close()