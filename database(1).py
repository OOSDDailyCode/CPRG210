#!/usr/bin/python3

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="harv",
    passwd="password",
    database="travelexperts")

cursor = conn.cursor()

sql = "select * from agents"
cursor.execute(sql)

result = cursor.fetchall()

for row in result:
    for col in row:
        print(str(col) + "\t")
    print("\n")
