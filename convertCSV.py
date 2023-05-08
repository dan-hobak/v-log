import re
import csv

# 로그 파일 경로
log_file_path = "resource/accesslog.txt"

# 분할된 로그를 저장할 CSV 파일 경로
csv_file_path = "resource/accesslog.csv"

# CSV 파일에 저장될 헤더
headers = ['IPAddress', 'Timestamp', 'Request', 'StatusCode', 'BytesSent', 'Referer', 'UserAgent']

# 로그를 분할할 정규식 패턴
log_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+) "(.*?)" "(.*?)"')

# CSV 파일에 저장할 데이터를 담을 리스트
data = []

# 로그 파일 열기
with open(log_file_path, 'r') as log_file:
    # 로그 파일의 각 줄을 읽어서 정규식 패턴과 매칭하여 데이터를 추출
    for line in log_file:
        match = log_pattern.match(line)
        if match:
            # 추출한 데이터를 리스트에 추가
            data.append(list(match.groups()))

# 추출한 데이터를 CSV 파일에 저장
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    writer.writerows(data)
