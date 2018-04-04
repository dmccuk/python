# get the api data from VRO

import requests

VRA = "https://server.local/some/location"
APP = "json.output"
username = "user1"
password = "password"

#print("Server=",VRA,"Application=",APP,"your user=",username,"Your password=",password)

url     = 'http://localhost/cis-page.html'
#payload = { 'key' : 'val' }
#headers = {}
#res = requests.post(url, data=payload, headers=headers)
#print(res)

web = requests.get(url)
keyword = web.text.find('Between the potential for Cyber attacks')
print (keyword)
#htmltext = web.text
#print(htmltext)

