#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 11:25
# @Author  : Dirk Zhao

import pymysql
from utils.ini_rw import ReadTest
from utils.log import logger

localReadConfig = ReadTest()


class MyDB:
    def __init__(self, database):
        host = localReadConfig.get_value('mysql', 'host')
        port = localReadConfig.get_value('mysql', 'port')
        username = localReadConfig.get_value('mysql', 'username')
        password = localReadConfig.get_value('mysql', 'password')
        self.config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database
        }

        self.db = None
        self.cursor = None

    def connect(self):
        try:
            self.db = pymysql.connect(**self.config)
            self.cursor = self.db.cursor()
        except ConnectionError as ex:
            logger.error(str(ex))

    def execute_sql(self, sql, params):
        self.connect()
        self.cursor.execute(sql, params)
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def close(self):
        self.db.close()
        print('Database closed')
