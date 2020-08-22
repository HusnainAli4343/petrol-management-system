from sqlite3 import *


def email_table():
    conn = connect("email_table.db")
    cur = conn.cursor()
    sqlQuery = """CREATE TABLE email_table (email TEXT, password TEXT)"""
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()



def email_data_inter(email, password):
    conn = connect("email_table.db")
    cur = conn.cursor()
    sqlQuery = """INSERT INTO email_table VALUES(""" + str(email) + "," + str(password) + ")"
    cur.execute(sqlQuery)
    # print(cur.fetchall())
    conn.commit()
    conn.close()

email_data_inter("Husnain", "Ali")


def read_e_C_T():
    conn = connect("email_table.db")
    cur = conn.cursor()
    sqlQuery = """SELECT * FROM  email_table"""
    cur.execute(sqlQuery)
    date_and_price = cur.fetchall()
    # return date_and_price
    print(date_and_price)
    conn.commit()
    conn.close()

# read_e_C_T()
