def deprecated_method_noncompliant(url):
    import botocore.vendored.requests as requests
    return requests.get(url)
