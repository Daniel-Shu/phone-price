#!/usr/bin/python

# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

def get_mysql_version():
    """TODO: Docstring for get_mysql_version.

    :returns: TODO

    """
    con = None
    try:

        # connect('ip','user','password','dbname')
        con = mdb.connect('localhost', 'testuser','test623', 'testdb');
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        data = cur.fetchone()
        print "Database version : %s " % data
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:
        if con:
            # remember to close it anyway
            con.close()


def create_table():
    """TODO: Docstring for insert_data.

    :returns: TODO

    """
    con = mdb.connect('localhost', 'testuser','test623', 'testdb');
    # only when we get the cursor, we can operate everything
    cur = con.cursor()
    '''
    # create a table   writers(id,name)
    cur.execute("CREATE TABLE IF NOT EXISTS \
                Writers(Id INT PRIMAY KEY AUTO_INCREMENT, Name VARCHAR(25))")

    # insert 6 pieces data
    cur.excute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.excute("INSERT INTO Writers(Name) VALUES('eetk London')")
    cur.excute("INSERT INTO Writers(Name) VALUES('fffh London')")
    cur.excute("INSERT INTO Writers(Name) VALUES('Jack 33333n')")
    cur.excute("INSERT INTO Writers(Name) VALUES('Jack 66666n')")
    cur.excute("INSERT INTO Writers(Name) VALUES('Jack 66777n')")
    '''
    # create a table
    cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # create the sql data
    sql_cmd = """
                CREATE TABLE EMPLOYEE(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT)"""

    cur.execute(sql_cmd)
    # close the connect
    con.close()


def insert_data():
    """TODO: Docstring for insert_data.

    :arg1: TODO
    :returns: TODO

    """
    con = mdb.connect('localhost', 'testuser','test623', 'testdb');
    # only when we get the cursor, we can operate everything
    cur = con.cursor()

    # sql insert data sentence
    sql = """
            INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX, INCOME)
            VALUES('MAC', 'Mohan', 20, 'M', 2000)"""
    '''
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
    '''

    try:
        #do the insert sentence
        cur.execute(sql)
        # commit it to the Database to excute
        con.commit()
    except Exception as e:
        # raise e
        # Rollback in case there is any error
        con.rollback()
        print e

    con.close()

def fetch_data():
    """TODO: Docstring for fetch_data.
    :returns: TODO

    """

    con = mdb.connect('localhost', 'testuser','test623', 'testdb');
    # only when we get the cursor, we can operate everything
    cur = con.cursor()

    # sql query sentence
    sql_cmd = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

    try:
        # execute the sql_cmd sentence
        cur.execute(sql_cmd)
        # get all the records
        result = cur.fetchall()
        for row in result:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]

        # print the rusult
        print "fname = %s, lname = %s, age = %d, sex = %s, income = %d" % (fname, lname, age, sex, income)
    except Exception as e:
        # raise e
        print e

    con.close()

if __name__ == '__main__':
    # get_mysql_version()
    # insert_data()
    # create_table()
    fetch_data()
