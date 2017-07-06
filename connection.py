import pymysql

# 打开数据库连接
connection = pymysql.connect("localhost", "root", "123456", "jwcoding", 3306)

try:

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `TABLE_NAME`,TABLE_COMMENT FROM information_schema.`TABLES` WHERE TABLE_SCHEMA=%s AND TABLE_TYPE='BASE TABLE'"
        cursor.execute(sql, ('jwcoding',))
        for i in range(cursor.rowcount):
            result = cursor.fetchone()
            print(result)

finally:
    connection.close()


def get_tables():
    pass
