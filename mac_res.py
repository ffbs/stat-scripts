#!/usr/bin/python
import csv
import sys
import sqlite3 as lite
import time
import get_clients
import ask_hwaddress
from sets import Set
import mac_add
con = lite.connect('mac.db')
with con:
	cur = con.cursor()
	# reader = list(csv.reader(f,delimiter=','))
	vendors = []
	client_count = 0
	print "unknown vendors:"
	macs = Set([])
	r_str = str(time.time()).split('.')[0] + ','
	#for client in get_clients.get_clients(True, "short"):# range(1, len(sys.argv)):
	#	aClient = client.split(':')
	#	pattern = "0x"+str(aClient[0])+str(aClient[1])+str(aClient[2])
	#	macs.add(pattern)
	macs = get_clients.get_clients(True, "short")
	for pattern in macs:
		vendor = ""
		client_count += 1
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
			man = ask_hwaddress.get_manu(pattern.split('x')[1])
			if man != None:
				mac_add.addKey(pattern, man)
				print "\t" + pattern + "  " + man
			else:
				print "\t" + pattern  
			vendor = "unknown"
		else:
			vendor = vendor[0]
			found = False
			try:
				for v in vendors:
					if v[0] == vendor:
						v[1] += 1
						found = True
				if not found:
					vendors.append([vendor, 1])
			except:
				vendors.append([vendor, 1])
	print "results:"
	persum = 0
	for v in vendors:
		per = (float(v[1]) / client_count)*100
		r_str += v[0] +  "," + str(v[1])+","
		persum += per
		print " %-40s %3d out of %3d clients = %2.2f %%" %(v[0], v[1], client_count, per)
	# print persum
	# print vendors
	with open("history.csv", "a") as myfile:
		myfile.write(r_str + "\n")
	myfile.close()
