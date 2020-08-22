from sqlite3 import *


def Diesel_table():
    conn = connect("Diesel.db")
    cur = conn.cursor()
    sqlQuery = """CREATE TABLE Diesel_Comming (Day integer, Month integer, Year integer, Litre integer, Price integer)"""
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()


def Diesel_inter(Day, Month, Year, Litre, Price):
    conn = connect("Diesel.db")
    cur = conn.cursor()
    sqlQuery = """INSERT INTO Diesel_Comming VALUES(""" + str(Day) + "," + str(Month) + "," + str(Year) + "," \
               + str(Litre) + "," + str(Price) + ")"
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()


def read_D_C_T():
    conn = connect("Diesel.db")
    cur = conn.cursor()
    sqlQuery = """SELECT * FROM  Diesel_Comming"""
    cur.execute(sqlQuery)
    date_and_price = cur.fetchall()
    # print(date_and_price)
    return date_and_price
    conn.commit()
    conn.close()


def Diesel_D_S_I_t():
    conn = connect("Diesel_Dally_Salling_and_income.db")
    cur = conn.cursor()
    sqlQuery = """CREATE TABLE Diesel_Dally_Salling_and_income (Day integer, Month integer, Year integer, Litre integer, Price integer)"""
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()


def Diesel_D_S_I(Day, Month, Year, Litre, Price):
    conn = connect("Diesel_Dally_Salling_and_income.db")
    cur = conn.cursor()
    sqlQuery = """INSERT INTO Diesel_Dally_Salling_and_income VALUES(""" + str(Day) + "," + str(Month) + "," + str(
        Year) + "," + str(Litre) + "," + str(Price) + ")"
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()


def read_D_S_i():
    conn = connect("Diesel_Dally_Salling_and_income.db")
    cur = conn.cursor()
    sqlQuery = """SELECT * FROM  Diesel_Dally_Salling_and_income"""
    cur.execute(sqlQuery)
    date_and_price = cur.fetchall()
    # print(date_and_price)
    return date_and_price
    conn.commit()
    conn.close()

