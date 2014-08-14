
try:
    from urllib2 import urlopen, HTTPError, Request  # Python 2
except:
    from urllib.request import urlopen, HTTPError, Request # Python 3

def get_page(url,username=None,password=None):
    request = Request(url)
    
    result = ""
    req = Request(url)
    if username and password:
        unamepw = "%s:%s" % (username, password)
        auth = base64.urlsafe_b64encode(unamepw)
        req.add_header("Authorization", "Basic %s" % auth)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print("URL: %s produced error %d (%s)" % (url,e.code,e.msg))
        print(auth_info)
    else:
        result = response.read()
    return result
    