#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pymysql

from util.readConfig import ReadConfig

mysql = ReadConfig()


class MysqlDb:
    def __init__(self):
        self.host = mysql.database("host")
        self.user = mysql.database("user")
        self.password = mysql.database("password")
        self.port = mysql.database("port")
        self.database = mysql.database("database")
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=3306,
                                    db=self.database, charset="utf8")

    def get_cursor(self):
        return self.conn.cursor()

    def query(self, sql):
        cursor = self.get_cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    test = MysqlDb()
    sql = "select * from sys_dict"
    data = test.query(sql)
    print(data)
