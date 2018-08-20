import requests
def httprequest(**req):
    res = requests.request(**req)
    return res