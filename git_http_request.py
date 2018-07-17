# importing the requests library
from flask_service import index
import requests, json, os, re, glob

# defining the api-endpoint

API_ENDPOINT = "https://api.github.com/repos/crhodes2/platform-samples/statuses/8da07da76b41230a67aae4a585f998b75a726f3b"
API_KEY = "18a0c4df0757c68f13767c0568e1bfc66169c512"
TO_POST = "http://localhost:5000/responseAPI"

# API_ENDPOINT = "https://api.github.com/repos/crhodes2/platform-samples/pulls/19"
# TO_POST = "http://localhost:5000/anotherAPI"
#
# # your API key here
# API_KEY = "18a0c4df0757c68f13767c0568e1bfc66169c512"
#
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

authentication = auth=('crhodes2', '18a0c4df0757c68f13767c0568e1bfc66169c512')
formattedAuth = ', '.join(authentication)
# # # getting get request and saving response as response object
# req = requests.post(url=API_ENDPOINT, data=data)
# jsonRequest = req.json()
# jsonRequestRead = ''.join(map(str, jsonRequest))
#
# # #sending post request and saving response as response object
# postReq = requests.post(url=TO_POST, auth=('crhodes2', API_KEY), json=json.dumps(jsonRequestRead))
# # postReq_Info = postReq.text
# print("POST REQUEST IS --> %s" % postReq.text)


headers = {'Authorization' : formattedAuth, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.post(TO_POST, headers=headers)

print("POST REQUEST IS --> %s" % r.text)