# 项目名：阿水AI
# 项目地址：https://ai.ashuiai.com/auth/register?inviteCode=C4566HBAK7
# 项目类型：网页
# 项目数据: 浏览器打开查看cookie,其中authorization就是,记得去掉 Bearer
# 环境变量: asai

import json
import os
import random
import time
import requests as r

def getUA():
    safari_version = f'{random.randint(600, 700)}.{random.randint(1, 4)}.{random.randint(1, 5)}'
    ios_version = f'{random.randint(12, 15)}.{random.randint(0, 6)}.{random.randint(0, 9)}'
    ua_string = f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/{safari_version} (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.20(0x16001422) NetType/WIFI Language/zh_CN'
    return ua_string

signUrl = 'https://api.xiabb.chat/chatapi/marketing/signin'

if os.environ.get("asai"):
    dvm = os.environ["asai"]
    if dvm != '':
        if "@" in dvm:
            Coo = dvm.split("@")
        else:
            Coo = dvm.split('\n')
    adv=1
    for i in Coo:
        headers = {
            "authority": "api.xiabb.chat",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN",
            "authorization": "Bearer "+i,
            "content-type": "application/json",
            "origin": "https://ai.ashuiai.com",
            "referer": "https://ai.ashuiai.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": getUA()
        }
        data = '^{^}'.encode('unicode_escape')
        req = r.post(signUrl,headers=headers,data=data)
        resp = json.loads(req.text)
        adv+=1
        # print(resp)
        if resp['code'] == 200:
            print("签到成功,获得20000token和5张绘画次数")
        elif resp['code'] == 500:
            print(resp['message'])
        else:
            print(resp)