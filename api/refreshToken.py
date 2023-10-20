import requests
import json
from helper import *
from config import RT, APP_SECRET, APP_ID

url += '/v2/user/refresh'
payload = json.dumps({
  "rt": RT
})

sign = makeSign(APP_SECRET, payload)

headers = {
  'X-CK-Nonce': nonce,
  'Authorization': f"Sign {sign}",
  'Content-Type': 'application/json',
  'X-CK-Appid': APP_ID
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
