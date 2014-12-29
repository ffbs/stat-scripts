#!/usr/bin/python2
import json
import urllib2
import time 
import yaml
import gzip
response = urllib2.urlopen('http://map.freifunk-bs.de/nodes.json')
html = response.read()
jsonData = json.loads(html)
aps = []
for link in jsonData['links']:
	if link.get('type') == "client":
		linkId = link.get('id')
		aLink = linkId.split('-')
		client = aLink[0].split(':')[0:3]
		client = int("0x"+client[0]+client[1]+client[2], 16)
		ap = aLink[1].split(':')[0:6]
		ap = int("0x"+ap[0]+ap[1]+ap[2]+ap[3]+ap[4]+ap[5], 16)
		found = False;
		for a in aps:
			if a[0] == ap:
				found = True
				a[1].append(client)
		if not found:
			aps.append([ap, [client]])
		aLog = [{'log': {'date':time.time(), 'aps': []}}]
for a in aps:
	aLog[0]['log']['aps'].append({'ap': a[0], 'clients': a[1]})
	#print str(a[0])+ " - " + str(a[1])
out = yaml.dump(aLog)
print out
f = gzip.open('client_links.yaml.gz', 'ab')
f.write(out)
f.close()



