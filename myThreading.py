# import time
#
# print("please wait...")
# time.sleep(10)
# print("time's up!")


import urllib, urllib3,urllib.request, json
with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
    data = json.loads(url.read().decode())
    print(data)