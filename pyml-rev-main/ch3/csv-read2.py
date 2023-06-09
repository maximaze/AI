import csv, codecs


# CSV 파일 열기
filename = "list-euckr.csv"
fp = codecs.open(filename, "r", "euc_kr")

# 한 줄씩 읽어 들이기 : 라인단위 처리
# 운영체제에 맞게 라인 구분자를 처리
# delimiter : 칼럼 구분자
# quotechar : 칼럼 데이터를 감싸고 있는 문자
reader = csv.reader(fp, delimiter=",", quotechar='"')

for cells in reader:
    print(cells[1], cells[2])

