import requests
import json
from helper import *
from config import AT

url += '/v2/device/thing'

payload = ""
headers = {
  'X-CK-Nonce': nonce,
  'Authorization': f"Bearer {AT}",
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
