from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test")  # 替換 TableName
    rows = cursor.fetchall()
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
