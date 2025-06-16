from flask import Flask, jsonify, request
from db import get_connection, insert_data

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test")
    rows = cursor.fetchall()
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    req = request.get_json()
    aaa = req.get('aaa')
    bbb = req.get('bbb')
    ccc = req.get('ccc')
    insert_data(aaa, bbb, ccc)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)