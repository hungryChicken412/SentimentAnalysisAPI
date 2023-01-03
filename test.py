# send a test simple post request to 174.138.2.127
# with text: "I want to talk to support"
# using requsts library

import requests
import json

url = "http://174.138.2.127/"
data = {
    "text": "I want to talk to support"
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)
