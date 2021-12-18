from pymysql import connect

conn = connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='my_data_base'
)
print(conn)
conn.close()