# Import all the files automation functions

from general import *
from ip_address import *
from domain_name import *
from nmap import *
from whois import *


# Create Reports 
def create_company_report(name, url, domain_name, ip_address, nmap, whois):
    project_dir = ROOT_DIRECTORY + '/' + name

    # Call the create_dir
    create_directory(project_dir)

    # Call the write_file function
    write_file(project_dir+'/url.txt',url)
    write_file(project_dir+'/domain_name.txt',domain_name)
    write_file(project_dir+'/ip_address.txt',ip_address)
    write_file(project_dir+'/nmap.txt',nmap)
    write_file(project_dir+'/whois.txt',whois)

# Gather all company data
def gather_company_info(name,url): 
 
    domain_name = get_domain_name(url) 
    ip_address = get_ip_address(domain_name) 
    nmap = get_nmap(' ',ip_address) 
    whois = get_whois(domain_name) 

    print "Domain Name is: ",domain_name
    print "IP address: ", ip_address
    print "Whois Information: ", whois
    print "Nmap Information: ", nmap

    # Call Create company reports
    create_company_report(name, url, domain_name, ip_address, nmap, whois)

# main function
print "Web Ninja code begins here \n"

# Main folder name.
ROOT_DIRECTORY = 'companies'

# call the create_dir function from the general.py file
create_directory(ROOT_DIRECTORY) 

#gather_info(company_name, url)
gather_company_info("facebook", "https://www.facebook.com")
