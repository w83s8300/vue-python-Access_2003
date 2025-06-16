import pyodbc

def get_connection():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Users\No978\Documents\Database1.mdb;'# 替換為你的 Access 資料庫路徑
    )
    return pyodbc.connect(conn_str)

def insert_data(aaa, bbb, ccc):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO test (AAA, bbb, ccc) VALUES (?, ?, ?)",
        (aaa, bbb, ccc)
    )
    conn.commit()
    conn.close()