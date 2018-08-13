import time, random
import hashlib
import urllib
import urllib.request
import json

url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"

app_key = 'rpicOvPJokTOivu7'
app_id = '2107795804'
questionS = '名字？'

def getSign(parser,appkey):
    sign_str = ''
    for key in sorted(parser.keys()):
        if parser[key] != "":
            sign_str += "%s=%s&"%(key, urllib.parse.quote(str(parser[key])))
    sign_str += "app_key=" + appkey
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper()
    return sign

class AiChat(object):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}
        self.session = ''

    def set_params(self, key, value):
        self.data[key] = value

    def getSign(self, parser, appkey):
        sign_str = ''
        for key in sorted(parser.keys()):
            if parser[key] != "":
                sign_str += "%s=%s&" % (key, urllib.parse.quote(str(parser[key])))
        sign_str += "app_key=" + appkey
        sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper()
        return sign

    def talk(self, question):
        question = question
        self.set_params("app_id", self.app_id)
        self.set_params("time_stamp", int(time.time()))
        self.set_params("nonce_str", str(random.random()))
        self.set_params("session", 10000)
        self.set_params("question", question)
        self.set_params("sign", self.getSign(self.data, self.app_key))
        print("------")
        print(self.data)
        data = urllib.parse.urlencode(self.data).encode("utf-8")
        request = urllib.request.Request(url, data=data)
        rsp = urllib.request.urlopen(request).read().decode("utf-8")
        # print(type(rsp))
        # print(rsp)
        rsp = json.loads(rsp)
        self.session = rsp["data"]["session"]
        if rsp["ret"] == 0:
            print("-----------------")
            print(rsp["data"]["answer"])
            print("-----------------")
        else:
            print(rsp["msg"])

    def talk2(self, question):
        question = question
        self.set_params("app_id", self.app_id)
        self.set_params("time_stamp", int(time.time()))
        self.set_params("nonce_str", str(random.random()))
        self.set_params("session", self.session)
        self.set_params("question", question)
        self.set_params("sign", self.getSign(self.data, self.app_key))
        print("------")
        print(self.data)
        data = urllib.parse.urlencode(self.data).encode("utf-8")
        request = urllib.request.Request(url, data=data)
        rsp = urllib.request.urlopen(request).read().decode("utf-8")
        # print(type(rsp))
        # print(rsp)
        rsp = json.loads(rsp)
        if rsp["ret"] == 0:
            print("-----------------")
            print(rsp["data"]["answer"])
            print("-----------------")
        else:
            print(rsp["msg"])


ai = AiChat(app_id, app_key)
while True:
    q = input("q")
    ai.talk(q)
    print(ai.data)
    # ai = AiChat(app_id, app_key)
    q = input("q2")
    ai.talk2(q)
    print(ai.data)