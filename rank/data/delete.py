#!/usr/bin/env python

import psycopg2

conn = psycopg2.connect(database="hpc", user="hpc", password="123456", host="localhost", port="5432")
print "Open database successfully"
cursor = conn.cursor()
cursor.execute("delete from rank_toponehundred;")
conn.commit()
conn.close()
