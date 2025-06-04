def domain_name(url):
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    url = url.replace("https://", "")
    s = url.split(".")
    
    return s[0]
    