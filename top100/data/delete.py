#!/usr/bin/env python

import psycopg2

conn = psycopg2.connect(database="hpc", user="hpc", password="rdcps@339", host="localhost", port="5432")
cursor = conn.cursor()
cursor.execute("delete from top100_ranking;")
conn.commit()
conn.close()
print "Delete database successfully"
