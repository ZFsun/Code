import urllib
import urllib.request
import time
import hashlib
import random
import json

# 获取签名
def getSign(parser,appkey):
    sign_str = ''
    for key in sorted(parser.keys()):
        if parser[key] != "":
            sign_str += "%s=%s&"%(key, urllib.parse.quote(str(parser[key])))
    sign_str += "app_key=" + appkey
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper()
    return sign

url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
# 通过注册腾讯api获取app_key和app_id
app_key = 'xxxxxxx'
app_id = 'xxxxxxx'
questionS = '你叫什么名字？'

params = {
    "app_id": app_id,
    "time_stamp":int(time.time()),
    "nonce_str": str(random.random()),
    "sign": "",
    "session": "10000",
    "question": questionS,
}
# 获取签名
sign = getSign(params, app_key)
params["sign"] = sign
# print(params)
data = urllib.parse.urlencode(params).encode("utf-8")

# 构造请求。如果Request()方法里的data参数有值，那么这个请求就是POST，如果没有，就是Get
request = urllib.request.Request(url, data = data)

# 返回数据
rsp = urllib.request.urlopen(request).read().decode("utf-8")

# 聊天回复
answer = json.loads(rsp)["data"]["answer"]
print(rsp)
print(answer)


