import os

print "This is the WHOIS File"
def get_whois(domain_name):
	command = "whois " + domain_name
	process = os.popen(command)
	data = str(process.read())
	return data


