#!/usr/bin/python
import csv
import sys
import sqlite3 as lite
import time
from sets import Set
con = lite.connect('mac.db')
with con:
	cur = con.cursor()
	# reader = list(csv.reader(f,delimiter=','))
	vendors=[]
	client_count = 0 
	print "unknown vendors:"
        macs = Set([])
	r_str = str(time.time()).split('.')[0] + ','
	for i in range(1,len(sys.argv)):
		a = sys.argv[i].split(':')
		pattern = "0x"+str(a[0])+str(a[1])+str(a[2])
                macs.add(pattern)
        for pattern in macs:
		vendor=""
		client_count +=1
		# for row in reader:
		# 	if pattern == row[0]:
		# 		# print row[1]
		# 		vendor = row[1]
		# 		break
		cur.execute("SELECT Vendor FROM Macs WHERE Mac LIKE '%s'"% pattern)
		con.commit()
		vendor = cur.fetchone()
		if vendor == None:
			# print "unknown"
			print "\t" + pattern
			vendor = "unknown"
		else:
			vendor = vendor[0]
		found = False
		try:
			for v in vendors:
				if v[0] == vendor:
					v[1]+=1
					found = True
			if not found:
				vendors.append([vendor,1])
		except:
			vendors.append([vendor,1])
	print "results:"
	persum = 0
	for v in vendors:
		per = (float(v[1]) / client_count)*100
		r_str += v[0] +  "," + str(v[1])+","
		persum += per
		print " %-40s %3d out of %3d clients = %2.2f %%" %(v[0],  v[1] , client_count , per) 
	# print persum
	# print vendors
	with open("history.csv", "a") as myfile:
		myfile.write(r_str + "\n")
	myfile.close()





	
