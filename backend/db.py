import pyodbc

def get_connection():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Users\No978\Documents\Database1.mdb;'# 替換為你的 Access 資料庫路徑
    )
    return pyodbc.connect(conn_str)
