import ConfigParser
import pymysql
import sqlite3
import os

class DButil(object):
    def __init__(self):
        sql3_lan_schema='''create table city (ID int NOT NULL, NAME TEXT NOT NULL, COUNTRYCODE TEXT NOT NULL, DISTRICT TEXT NOT NULL, Population int NOT NULL)''' 
        conn=sqlite3.connect('test.db')
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')

        try:
            mysql_conn = pymysql.connect(user='root',password='root123',host='localhost')
        except exception as e:
            print e

        mysql_cursor=mysql_conn.cursor()
        mysql_cursor.execute('''select * from world.city''')
        res=mysql_cursor.fetchall()
        conn.executescript(sql3_lan_schema)
        conn.executemany("insert into city values (?,?,?,?,?)",res)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    DButil()
