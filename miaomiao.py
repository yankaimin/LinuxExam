#!/usr/bin/python3
import time
import hmac
import hashlib
import base64
import urllib.parse
import io
import requests, json  # 导入依赖库
import sys

class DingDingHandler:
    def __init__(self, token, secret):
        self.token = token
        self.secret = secret

    def get_url(self):
        timestamp = round(time.time() * 1000)
        secret_enc = self.secret.encode("utf-8")
        string_to_sign = "{}\n{}".format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode("utf-8")
        hmac_code = hmac.new(
            secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
        ).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=SEC8f46922de4496a3d2c1c67a2f4fa41f0dcd9550835fd47f5dcf4bcfcf75382b2

        )
        return api_url

    def ddlinksend(self, link, text, title):
        headers = {"Content-Type": "application/json"}  # 定义数据类型
        data = {
            "msgtype": "link",
            "link": {
                "text": text,
                "title": title, 
                "messageUrl": link,
            },
        }
        res = requests.post(self.get_url(), data=json.dumps(data), headers=headers)  # 发送post请求
        print(res.text)

    def ddtextsend(self, m):
        headers = {"Content-Type": "application/json"}  # 定义数据类型
        data = {
            "msgtype": "text",
            "text": {

                "content":"严凯敏的CPU"+m
            },
        }
        res = requests.post(self.get_url(), data=json.dumps(data), headers=headers)  # 发送post请求
        print(res.text)

m = sys.argv[1]
token="38792ee6d7a1bba223e6dff43b2d8ba1c4276b8a57cbc8bd8f6ca0c3e7bdc30f"
secret="SEC8f46922de4496a3d2c1c67a2f4fa41f0dcd9550835fd47f5dcf4bcfcf75382b2"
dingDingHandler =DingDingHandler(token,secret)
dingDingHandler.ddtextsend(m)
