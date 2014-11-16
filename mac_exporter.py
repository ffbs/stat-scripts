#!/usr/bin/python
import sqlite3 as lite
con = lite.connect('mac.db')
with con:
	cur = con.cursor()
	vendor=None
	cur.execute("SELECT * FROM Macs")
	con.commit()
	vendor = cur.fetchone()
	i=0
	while(vendor ):
		vendor = cur.fetchone()
		i+=1
		try:
			print "%s,%s"% (vendor[0],vendor[1])
		except:
  			pass 

