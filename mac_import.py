#!/usr/bin/python
import sqlite3 as lite
import sys
import csv
con = lite.connect('mac.db')
with open(sys.argv[1]) as f:
	r = csv.reader(f,delimiter=',')
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE Macs")
		cur.execute("CREATE TABLE Macs(Mac TEXT PRIMARY KEY, Vendor TEXT)")
		vendor=None
		for line in r:
			#print line
			cur.execute("INSERT INTO Macs VALUES(?,?)",(line[0],line[1]))
		con.commit()
