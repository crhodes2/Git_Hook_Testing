# importing the requests library
from flask_service import index
import requests, json, os, re, glob

# defining the api-endpoint

#API_ENDPOINT = "http://localhost:5000"
API_ENDPOINT = "https://api.github.com/repos/crhodes2/platform-samples/pulls/19"
TO_POST = "http://localhost:5000/anotherAPI"

# your API key here
API_KEY = "18a0c4df0757c68f13767c0568e1bfc66169c512"

# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
c = a + b
print(c)
'''

# data to be sent to api
data = {'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': source_code,
        'api_paste_format': 'python'}

# getting get request and saving response as response object
req = requests.get(url=API_ENDPOINT, data=data)
jsonRequest = req.json()
print(jsonRequest)

# jsonRequest[0]["first"] = "Galen"

#sending post request and saving response as response object
postReq = requests.post(url=TO_POST, auth=('crhodes2', API_KEY), json=json.dumps(jsonRequest))
postReq_Info = postReq.text
print("POST REQUEST IS --> %s" % postReq_Info)

# extracting response text
#pastebin_url = r.text
#print("The pastebin URL is:%s" % pastebin_url)