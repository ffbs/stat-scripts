#!/usr/bin/python2
import json
import urllib2
def get_clients(onlyVendor = False, encoding = "normal"):
	response = urllib2.urlopen('http://map.freifunk-bs.de/nodes.json')
	html = response.read()
	jsonData = json.loads(html)
	nodes = []
	for node in jsonData['nodes']:
		if node.get('flags')['client'] == True:
			inode = node.get('macs')
			if onlyVendor:
				aClient = inode.split(':')
				if encoding == "short":
					nodes.append("0x"+str(aClient[0])+str(aClient[1])+str(aClient[2]))
				else:
					nodes.append(str(aClient[0])+":"+str(aClient[1])+":"+str(aClient[2]))
			else:
				nodes.append(node.get('macs'))
				aClient = inode.split(':')
				if encoding == "short":
					nodes.append("0x"+str(aClient[0])+str(aClient[1])+str(aClient[2])+str(aClient[3])+str(aClient[4])+str(aClient[5]))
				else:
					nodes.append(str(aClient[0])+":"+str(aClient[1])+":"+str(aClient[2])+":"+str(aClient[3])+":"+str(aClient[4])+":"+str(aClient[5]))
	return nodes

if __name__ == "__main__":
	clients = get_clients()
	for i in clients:
		print i

