#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import datetime
import get_phone_price

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

ip = 'localhost'
user = 'testuser'
pwd  = 'test623'
dbname = 'testdb'

def get_mysql_version():
    """TODO: Docstring for get_mysql_version.

    :returns: TODO

    """
    con = None
    try:

        # connect('ip','user','password','dbname')
        con = mdb.connect(ip, user, pwd, dbname)
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
    con = mdb.connect(ip, user, pwd, dbname)
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
    cur.execute("DROP TABLE IF EXISTS PRICE")
    # create the sql data
    sql_cmd = """
                CREATE TABLE EMPLOYEE(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT)"""
    sql_cmd_create_price = """CREATE TABLE PRICE(
                                ID BIGINT UNSIGNED NOT NULL,
                                NAME TEXT,
                                URL TEXT)"""
    cur.execute(sql_cmd_create_price)
    # close the connect
    con.close()


def insert_data(arg1):
    """TODO: Docstring for insert_data.

    :arg1: TODO
    :returns: TODO

    """
    con = mdb.connect(ip, user, pwd, dbname)
    # only when we get the cursor, we can operate everything
    cur = con.cursor()

    # sql insert data sentence

    '''
    sql = """
            INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX, INCOME)
            VALUES('中MAC', 'Mohan', 20, 'M', 2000)"""


    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ("中文c", 'Mohan', 20, 'M', 2000)

    '''
    # we can insert like this (including chinese)
    sql = "INSERT IGNORE INTO PRICE(ID,NAME, URL) \
       VALUES ('%d', '%s', '%s')" % \
       (long(arg1["Id"]), arg1["Name"].encode('utf-8'), arg1["Url"].encode('utf-8'))
    # we can insert the data by judge if it exists like this
    sql = "INSERT IGNORE INTO PRICE(ID, NAME, URL) \
        SELECT '%d','%s','%s' FROM DUAL \
        WHERE NOT EXISTS(SELECT ID FROM PRICE WHERE ID=%d)" %\
       (long(arg1["Id"]), arg1["Name"].encode('utf-8'), arg1["Url"].encode('utf-8'), long(arg1["Id"]))

    try:
        #do the insert sentence
        cur.execute(sql)          # this the insert cmd
        # commit it to the Database to excute
        con.commit()
    except Exception as e:
        # raise e
        # Rollback in case there is any error
        con.rollback()
        print e

    con.close()

def update_price(arg1, setornot):
    """TODO: Docstring for update_price.

    :arg1: TODO
    :returns: TODO

    """

    con = mdb.connect(ip, user, pwd, dbname)
    # only when we get the cursor, we can operate everything
    cur = con.cursor()

    today = arg1["Date"]
    # prepare the add price and commit set cmd
    price_date_set = "PRICE_" + str(today)
    sql_cmd_add_price_set = "ALTER TABLE PRICE ADD %s FLOAT" % (price_date_set)
    commit_date_set = "COMMIT_" + str(today)
    sql_cmd_add_commit_set= "ALTER TABLE PRICE ADD %s INT UNSIGNED" % (commit_date_set)
    if (setornot == 0):
        try:
            cur.execute(sql_cmd_add_price_set)
            cur.execute(sql_cmd_add_commit_set)
        except Exception as e:
            print "This error is in the add set process"
            print e
    # temp = "ALTER TABLE EMPLOYEE CHANGE DATE DATE DATE NOT NULL DEFAULT CURRENT_DATE()"
    # sql_cmd_set_default = "ALTER TABLE EMPLOYEE ALTER COLUMN DATE SET DEFAULT '2016-05-22'"
    # sql_cmd_update = "UPDATE EMPLOYEE DATE='2010-10-10'"

    # prepare the cmd to update the price and the commit when the condition is ok
    sql_cmd_update_price = "UPDATE PRICE SET %s = %f WHERE ID = %d" % (price_date_set, float(arg1["Price"]), int(arg1["Id"]))
    sql_cmd_update_commit= "UPDATE PRICE SET %s = %f WHERE ID = %d" % (commit_date_set, int(arg1["Commit"]), int(arg1["Id"]))


    try:
        #do the update cmd
        cur.execute(sql_cmd_update_price)
        cur.execute(sql_cmd_update_commit)
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

    con = mdb.connect(ip, user, pwd, dbname)
    # only when we get the cursor, we can operate everything
    cur = con.cursor()

    # sql query sentence
    # sql_cmd = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
    sql_cmd = "SELECT * FROM PRICE"

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
            print lname

        # print the rusult
        # print "fname = %s, lname = %s, age = %d, sex = %s, income = %d" % (fname, lname, age, sex, income)
    except Exception as e:
        # raise e
        print e

    con.close()

if __name__ == '__main__':
    # get_mysql_version()
    # insert_data()
    # create_table()
    # fetch_data()

    temp = 0
    page = 3
    url = "http://list.jd.com/list.html?cat=9987%2C653%2C655&page=1"
    for i in range(1,page + 1):
        url += str(i)
        info_dict_array = get_phone_price.get_phone_info(url)
        for item in info_dict_array:
            insert_data(item)
            update_price(item, temp)
            temp += 1
