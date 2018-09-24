#!/usr/bin/python3
# coding: utf-8
import os
import pickle

import pymysql

file_db = os.path.join(os.getcwd(), 'db.sqlite3')
totals = 'data.pkl'


def insert_data(items):
    # sql = """
    # insert into blog_blog(id, title, slug, category, date_time, content) values (?, ?, ?, ?, ?, ?)
    # """
    sql = """
    insert into blog_blog(id, title, slug, category, date_time, content) values (%s, %s, %s, %s, %s, %s)
    """

    # conn = sqlite3.connect(file_db)

    from config import bwg_database

    host = bwg_database.get('HOST')
    name = bwg_database.get('NAME')
    user = bwg_database.get('USER')
    password = bwg_database.get('PASSWORD')
    port = bwg_database.get('PORT')

    conn = pymysql.connect(host=host, user=user,
                           passwd=password, db=name,
                           port=int(port))
    cur = conn.cursor()

    for item in items:
        print(item[1])
        cur.execute(sql, item)
    conn.commit()
    conn.close()


def main():
    with open(totals, 'rb') as f:
        total = pickle.load(f)

    insert_data(total)


if __name__ == '__main__':
    main()
