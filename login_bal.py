# -*- coding:utf-8 -*-
import random

# !/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib3
from urllib.parse import urlencode


def send_code_by_message(cell_no, validation_code):
    url = "http://v.juhe.cn/sms/send"
    params = {
        "mobile": cell_no,  # 接受短信的用户手机号码
        "tpl_id": "162718",  # 您申请的短信模板ID，根据实际情况修改
        "tpl_value": "#code#=%s" % validation_code,  # 您设置的模板变量，根据实际情况修改
        "key": "62f148ec799f313ae5a04b18ecd85e24",  # 应用APPKEY(应用详细页查询)
    }
    http = urllib3.PoolManager()
    #params = urlencode(params)
    f = http.request("GET", url,
                     fields=params)
    content = f.data.decode()
    print(content)
    res = json.loads(content)
    if res and res["error_code"] == 0:
        return 1
    else:
        return -1


def generate_validation_code(cell_no):
    """"
    根据手机号生成对应的验证码
    """
    codes = "".join([str(random.randint(100, 1000) % 10) for _ in range(6)])
    status = send_code_by_message(cell_no, codes)
    return codes, status
