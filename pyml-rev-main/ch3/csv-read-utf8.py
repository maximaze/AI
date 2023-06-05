import codecs


# UTF-8로 저장된 CSV 파일 읽기
filename = "list-utf-8.csv"
csv = codecs.open(filename, "r", "utf-8").read()

# CSV을 파이썬 리스트로 변환하기
data = []
# rows = csv.split("\r\n")
rows = csv.split("\n")

for row in rows:
    if row == "": continue
    cells = row.split(",")
    print('cells:', cells)
    data.append(cells)

# 결과 출력하기
print("[결과]")
for c in data:
    print(c[0], c[1], c[2])

