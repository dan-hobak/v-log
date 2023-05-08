import pandas as pd
import sqlite3

# CSV 파일 경로
csv_file_path = "resource/accesslog.csv"

# 데이터베이스 경로
db_file_path = "resource/accesslog.db"

# 데이터베이스 연결 생성
conn = sqlite3.connect(db_file_path)

# 테이블 삭제
conn.execute("DROP TABLE IF EXISTS accesslog")

# CSV 파일을 pandas DataFrame으로 읽어들이기
df = pd.read_csv(csv_file_path)

# DataFrame을 SQLite 데이터베이스에 쓰기
df.to_sql('accesslog', conn)

# 커밋과 연결 닫기
conn.commit()
conn.close()
