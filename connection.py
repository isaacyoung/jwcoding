import pymysql

# 打开数据库连接
from config import Config


def connect():
    return pymysql.connect(Config.get_host(), Config.get_prop('jdbc.username'), Config.get_prop('jdbc.password'),
                           Config.get_database(), int(Config.get_port()), charset='utf8')


def get_tables():
    connection = connect()
    try:
        result = []
        with connection.cursor() as cursor:
            sql = "SELECT `TABLE_NAME`,TABLE_COMMENT FROM information_schema.`TABLES` WHERE TABLE_SCHEMA=%s AND TABLE_TYPE='BASE TABLE' ;"
            cursor.execute(sql, (Config.get_database()))
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                result.append(row)

        return result
    finally:
        connection.close()


def get_table(t):
    connection = connect()
    try:
        result = []
        with connection.cursor() as cursor:
            sql = "SELECT `TABLE_NAME`,TABLE_COMMENT FROM information_schema.`TABLES` WHERE TABLE_SCHEMA=%s AND TABLE_TYPE='BASE TABLE' AND `TABLE_NAME`=%s ;"
            cursor.execute(sql, (Config.get_database(), t))
            row = cursor.fetchone()
            result.append(row)

        return result
    finally:
        connection.close()


def get_columns(t):
    connection = connect()
    try:
        result = []
        with connection.cursor() as cursor:
            sql = "SELECT `TABLE_NAME`,`COLUMN_NAME`,COLUMN_KEY,DATA_TYPE,NUMERIC_SCALE,CHARACTER_MAXIMUM_LENGTH,COLUMN_COMMENT FROM information_schema.`COLUMNS` WHERE TABLE_SCHEMA=%s AND `TABLE_NAME`=%s ;"
            cursor.execute(sql, (Config.get_database(), t))
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                result.append(row)

        return result
    finally:
        connection.close()

