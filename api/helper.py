import base64
import hashlib
import hmac
import random
import string

from config import REGION


def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def makeSign(key:str, message:str) -> str:
    return (base64.b64encode(hmac.new(key.encode(), message.encode(), digestmod=hashlib.sha256).digest())).decode()


url = f"https://{REGION}-apia.coolkit.cc"
nonce = random_string(8)