import requests
import json
from helper import *
from config import AT

device_id = '10017d680c'
url += f"/v2/device/thing/status?type=1&id={device_id}&params=switch|pulse"

payload = ""

headers = {
  'X-CK-Nonce': nonce,
  'Authorization': f"Bearer {AT}",
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
