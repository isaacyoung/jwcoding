import pymysql

# 打开数据库连接


def connect():
    return pymysql.connect("localhost", "root", "123456", "jwcoding", 3306)


def get_tables():
    connection = connect()
    try:
        result = []
        with connection.cursor() as cursor:
            sql = "SELECT `TABLE_NAME`,TABLE_COMMENT FROM information_schema.`TABLES` WHERE TABLE_SCHEMA=%s AND TABLE_TYPE='BASE TABLE'"
            cursor.execute(sql, ('jwcoding',))
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                result.append(row)

        return result
    finally:
        connection.close()

