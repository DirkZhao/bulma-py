#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 10:44
# @Author  : Dirk Zhao
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from utils.log import logger
from utils.httpm import HttpM
from config.config import DATA_PATH


localConfigHttp = HttpM()
database = {}


def get_xls(file, sheet):
    cls = []
    path = os.path.join(DATA_PATH, file)
    file = open_workbook(path)
    sheet = file.sheet_by_name(sheet)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(DATA_PATH, 'sql.xml')
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table


def get_xml_dict(database_name, table):
    set_xml()
    db_dict = database.get(database_name).get(table)
    return db_dict


def get_sql(database_name, table, sql_id):
    db = get_xml_dict(database_name, table)
    sql = db.get(sql_id)
    return sql
