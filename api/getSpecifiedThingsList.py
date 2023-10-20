import requests
import json
from helper import *
from config import AT

url += '/v2/device/thing'

payload = json.dumps({
  "thingList": [
    {
      "itemType": 1,
      "id": "10017d680c"
    }
  ]
})

headers = {
  'X-CK-Nonce': nonce,
  'Authorization': f"Bearer {AT}",
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
