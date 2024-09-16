
def http_request_noncompliant(username, password, url):
    import urllib3 as urllib3
    from base64 import b64encode
    userpass = "%s:%s" % (username, password)
    authorization = b64encode(str.encode(userpass)).decode("utf-8")
    headers = {'Authorization': 'Basic %s' % authorization}
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    response = http.request('GET', url, headers=headers)
