#!/usr/bin/python
import sqlite3 as lite
import sys
import csv
con = lite.connect('mac.db')
with con:
	cur = con.cursor()
	vendor=None
	cur.execute("INSERT INTO Macs VALUES(?,?)",(sys.argv[1],sys.argv[2]))
	con.commit()
	cur.execute("SELECT * FROM Macs WHERE Mac LIKE '%s'"% sys.argv[1])
	vendor = cur.fetchone()
	print vendor
