from flask import Flask, redirect, request
import hashlib
import hmac
import base64
import time
import random
import string 
from config import APP_ID, APP_SECRET, REDIRECT_URL

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def makeSign(key:str, message:str) -> str:
    return (base64.b64encode(hmac.new(key.encode(), message.encode(), digestmod=hashlib.sha256).digest())).decode()

user_id = random_string(8)
nonce = random_string(8)
t_now = int(time.time())

sign = makeSign(APP_SECRET, f"{APP_ID}_{t_now}")

app = Flask(__name__)

@app.route("/redirectUrl")
def hello_world():
    return f"code {request.args.get('code')}<br>region {request.args.get('region')} <br>state {request.args.get('state')}"

@app.route("/login")
def login():
    return redirect(f"https://c2ccdn.coolkit.cc/oauth/index.html?state={user_id}&clientId={APP_ID}&authorization={sign}&seq={t_now}&redirectUrl={REDIRECT_URL}&nonce={nonce}&grantType=authorization_code", code=302)