import openpyxl 


# 엑셀 파일 열기く --- (※1)
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기 --- (※2)
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기 --- (※3)
data = []
for row in sheet.rows:
    data.append([
        row[0].value, # 지역이름
        row[10].value # 2018년도
    ])

# 필요없는 줄(헤더, 연도, 계) 제거하기
del data[0:3]

# del data[0]
# del data[1]
# del data[2]

print(data)

# 데이터를 인구 순서로 정렬합니다.
# 오름차순 : 인구가 작은 값에서 큰 값으로 정렬
data = sorted(data, key=lambda x:x[1])

# 하위 5위를 출력합니다.
for i, a in enumerate(data):
    if (i >= 5): break
    print(i+1, a[0], int(a[1]))

