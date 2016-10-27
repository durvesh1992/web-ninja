import os

#function to fetch IP address
def get_ip_address(url):
    print " URL: ",url
    print "Fetching IP address...\n"
    command = "host "+ url

    #open the CLI
    process = os.popen(command)

    data = str(process.read())
    marker = data.find("has address") + 12
    print "Result is : ",data

    #marker is used to store the index value from where we can get the further elements in the array
    return data[marker:]

#print (get_ip_address('glassdoor.com/'))
