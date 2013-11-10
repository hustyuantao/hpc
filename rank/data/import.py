#!/usr/bin/env python

import psycopg2

conn = psycopg2.connect(database="hpc", user="hpc", password="123456", host="localhost", port="5432")
print "Open database successfully"
cursor = conn.cursor()
data_list = [(2, '2003.txt'), (3, '2004.txt'), (4, '2005.txt'), (5, '2006.txt'), (6, '2007.txt'), (7, '2008.txt'), (8, '2009.txt'), (9, '2010.txt'), (10, '2011.txt'), (11, '2012.txt')]
for nth, name in data_list:
	file = open(name)
	while True:
		rank = file.readline()
		if not rank:
			break
		manufacturer = file.readline().strip()
		computer = file.readline().strip()
		site = file.readline().strip()
		year = file.readline().strip()
		segment = file.readline().strip()
		total_cores = file.readline().strip()
		rmax = file.readline().strip()
		reference = file.readline().strip()
		rpeak = file.readline().strip()
		efficiency = file.readline().strip()
		#print "INSERT INTO rank_toponehundred (nth, rank, manufacturer, computer, site, year, segment, total_cores, rmax, reference, rpeak, efficiency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (nth, rank, manufacturer, computer, site, year, segment, total_cores, rmax, reference, rpeak, efficiency)
		cursor.execute("INSERT INTO rank_toponehundred (nth, rank, manufacturer, computer, site, year, segment, total_cores, rmax, reference, rpeak, efficiency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (nth, rank, manufacturer, computer, site, year, segment, total_cores, rmax, reference, rpeak, efficiency))
conn.commit()
conn.close()
