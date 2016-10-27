# Domain name from the URL
def get_domain_name(url):

    results = url
    str(results)

    # check whether http or https
    flag = results[:5]
    if flag == 'https':
        domain_name = get_https_domain(url)
    else:
        domain_name = get_http_domain(url)

    #return value to the main
    return domain_name


#https function 
def get_https_domain(url):
    marker = url[12:]
    return marker

#http function 
def get_http_domain(url):
    marker = url[11:]
    return marker


