import mysql.connector
from tabulate import tabulate
from dotenv import load_dotenv
import os

def get_tables_and_row_count(host, user, password, database):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    table_data = []
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
        count = cursor.fetchone()
        table_data.append([table[0], count[0]])

    cursor.close()
    db.close()

    return table_data


# .envファイルの内容をロード
load_dotenv()

host = os.getenv("DB_HOST", "localhost")  # デフォルト値としてlocalhostを設定
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
database = os.getenv("DB_NAME")

tables_and_counts = get_tables_and_row_count(host, user, password, database)

# tabulateを使って結果をきれいに表示
print(tabulate(tables_and_counts, headers=["Table", "Row Count"], tablefmt="pretty"))
