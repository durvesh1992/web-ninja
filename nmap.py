import os

def get_nmap(options,ip):
	print "NMAP (Network Mapper) is activated!! \n "
	command = "nmap " + options + " " + ip
	process = os.popen(command)
	data = str(process.read())
	return data



