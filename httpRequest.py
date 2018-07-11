# importing the requests library
import requests, json

# defining the api-endpoint
API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "1234567889abcdefxyz"

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

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)
#print(r.json())

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)