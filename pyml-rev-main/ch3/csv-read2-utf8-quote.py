import csv, codecs


# CSV 파일 열기 : UTF-8, 큰따옴표로 감쌈
# 파일의 인코딩이 utf-8로 되어있어야됨
filename = "list-utf-8-quote2.csv"
fp = codecs.open(filename, "r", "utf-8")

# 한 줄씩 읽어 들이기 : 라인단위 처리
# 운영체제에 맞게 라인 구분자를 처리
# delimiter : 칼럼 구분자
# quotechar : 칼럼 데이터를 감싸고 있는 문자
reader = csv.reader(fp, delimiter=",", quotechar='"')

for cells in reader:
    print(f"[{cells[0]}],[{cells[1]}], [{cells[2]}]")

