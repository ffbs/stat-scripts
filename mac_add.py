#!/usr/bin/python
import sqlite3 as lite
import sys
import csv
def addKey(mac, vendor):
	con = lite.connect('mac.db')
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO Macs VALUES(?,?)",(mac, vendor))
		con.commit()
		cur.execute("SELECT * FROM Macs WHERE Mac LIKE '%s'"% mac)
		vendor = cur.fetchone()
