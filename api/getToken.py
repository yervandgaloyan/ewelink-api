import requests
import json
from config import CODE, REDIRECT_URL, APP_ID, APP_SECRET
from helper import *

url += '/v2/user/oauth/token'

payload = json.dumps({
  "code": CODE,
  "redirectUrl": REDIRECT_URL,
  "grantType": "authorization_code"
})
sign = makeSign(APP_SECRET, payload)

headers = {
  'X-CK-Nonce': 'kh1fYBfn',
  'Authorization': f"Sign {sign}",
  'Content-Type': 'application/json',
  'X-CK-Appid': APP_ID
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)