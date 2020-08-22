from sqlite3 import *


# ======================== Petrol jo aya ====================
def Petrol_table():
    conn = connect("Petrol.db")
    cur = conn.cursor()
    sqlQuery = """CREATE TABLE Petrol_Comming (Day integer, Month integer, Year integer, Litre integer, Price integer)"""
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()

# ======================== Petrol jis din aya ir katna aya or us ki price====================

def Petrol_inter(Day, Month, Year, Litre, Price):
    conn = connect("Petrol.db")
    cur = conn.cursor()
    sqlQuery = """INSERT INTO Petrol_Comming VALUES(""" + str(Day) + "," + str(Month) + "," + str(Year) + "," \
               + str(Litre) + "," + str(Price) + ")"
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()

# ================== us ka data nikalana ka kaya ===================================

def read_total_petrol_amount():
    conn = connect("Petrol.db")
    cur = conn.cursor()
    sqlQuery = """SELECT * FROM  Petrol_Comming"""
    cur.execute(sqlQuery)
    date_and_price = cur.fetchall()
    # print(date_and_price)
    return date_and_price
    conn.commit()
    conn.close()
read_total_petrol_amount()

#=============================== rozana ka Data enter karna k laya table banaya gaya ==================


def petrol_D_S_I_t():
    conn = connect("Petrol_Dally_Salling_and_income.db")
    cur = conn.cursor()
    sqlQuery = """CREATE TABLE Petrol_Dally_Salling_and_income (Day integer, Month integer, Year integer, Litre integer, Price integer)"""
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()

#=============================== rozana ka Data enter karna k laya table banaya gay table ma Data Entry karna k laya ==================


def petrol_daily_selling_amount(Day, Month, Year, Litre, Price):
    conn = connect("Petrol_Dally_Salling_and_income.db")
    cur = conn.cursor()
    sqlQuery = """INSERT INTO Petrol_Dally_Salling_and_income VALUES(""" + str(Day) + "," + str(Month) + "," + str(
        Year) + "," + str(Litre) + "," + str(Price) + ")"
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()

#=============================== rozana ka Data enter karna k laya table banaya gay ko dakana k laya ==================


def petrol_daily_selling_details():
    conn = connect("Petrol_Dally_Salling_and_income.db")
    cur = conn.cursor()
    sqlQuery = """SELECT * FROM  Petrol_Dally_Salling_and_income"""
    cur.execute(sqlQuery)
    date_and_price = cur.fetchall()
    # print(date_and_price)
    return date_and_price
    conn.commit()
    conn.close()

#
# def income_table():
#     conn = connect("Petrol_Remaining.db")
#     cur = conn.cursor()
#     sqlQuery = """CREATE TABLE Petrol_Remaining (Day integer, Month integer, Year integer, Litre integer, Price integer)"""
#     cur.execute(sqlQuery)
#     conn.commit()
#     conn.close()
#
#
# def derived_Data(d, m, y):
#     d =str(d)
#     m = str(m)
#     y = str(y)
#     conn = connect("Petrol.db")
#     cur = conn.cursor()
#     sqlQuery = "SELECT * FROM  Petrol_Comming WHERE Day =", d, "AND Month = ", m, " AND Year = ", y, ""
#     cur.execute(sqlQuery)
#     date_and_price = cur.fetchall()
#     print(date_and_price)
#     # return date_and_price
#     conn.commit()
#     conn.close()
#
# derived_Data(1,7,2020)
#
# def petrol_D_i(Day, Month, Year, Litre, Price):
#     conn = connect("Petrol_Remaining.db")
#     cur = conn.cursor()
#     sqlQuery = """INSERT INTO Petrol_Remaining VALUES(""" + str(Day) + "," + str(Month) + "," + str(
#         Year) + "," + str(Litre) + "," + str(Price) + ")"
#     cur.execute(sqlQuery)
#     conn.commit()
#     conn.close()
#
