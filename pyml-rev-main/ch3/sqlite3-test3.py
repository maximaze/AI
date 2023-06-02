import sqlite3


# sqlite 데이터베이스 연결하기 --- (※1)
dbpath = "items.sqlite"
conn = sqlite3.connect(dbpath)

# 데이터 추출하기 --- (※4)
cur = conn.cursor()
cur.execute("SELECT item_id,name,price FROM items")
item_list = cur.fetchall()

print('item_list: ', type(item_list)) # <class 'list>
    
# 출력하기
for it in item_list:
    print(type(it), ': ',it)

# 종료
conn.close()

