import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 데이터베이스 경로
db_file_path = "resource/accesslog.db"

# 데이터베이스 연결 생성
conn = sqlite3.connect(db_file_path)

# 가장 많은 트래픽을 발생시킨 상위 5개 IP 주소를 출력하는 쿼리문 실행
query = "SELECT `IPAddress`, COUNT(*) AS `Count` FROM `accesslog` GROUP BY `IPAddress` ORDER BY `Count` DESC LIMIT 5"
result = conn.execute(query)

# 결과를 pandas DataFrame으로 변환
df = pd.DataFrame(result.fetchall(), columns=["IP Address", "Count"])

# 시각화
plt.bar(df["IP Address"], df["Count"])
plt.title("Top 5 IP Addresses by Traffic")
plt.xlabel("IP Address")
plt.ylabel("Traffic Count")
plt.show()

# 연결 닫기
conn.close()
