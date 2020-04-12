# import  configparser
#
# config=configparser.ConfigParser()
# config.read('config.ini',encoding='GB18030')
# print(config.sections())
# print(config.options('path'))
# print(config.items('path'))

dict_01={'t':"1234","h":"345"}


# tt=dict_01.keys()

# def tanghuan(d,code):
#     if isinstance(d,dict) and  code in d.keys() :
#         print(d)
#     elif isinstance(d,(list,int)):
#         print('ffffffffff')
#     else:
#         print('错误')
# tanghuan(dict_01,'t')

import json

# json文件发送形式
SendRegisterVerificationCodejson_txt = """
{
  "header":{
    "funcNo": "IF010002",
    "opStation": "11.11.1.1",
    "appId": "aaaaaa",
    "deviceId": "kk",
    "ver":"wx-1.0",
    "channel": "4"
  },
  "payload": {
    "mobileTel": "13817120001"
  }
}
"""
print(type(SendRegisterVerificationCodejson_txt))
date_json = json.loads(SendRegisterVerificationCodejson_txt)
print(type(date_json))
print("*" * 10)
# 发送时，每次需要注册新的手机号码，就需要json每次提示mobileTel的value进行发送
# 遍历json文件所有的key对应的value
dic = {}

def json_txt(dic_json):
    if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
        for key in dic_json:
            if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
                print("111****key--：%s value--: %s" % (key, dic_json[key]))
                json_txt(dic_json[key])

                dic[key] = dic_json[key]
            else:
                print("222****key--：%s value--: %s" % (key, dic_json[key]))
                dic[key] = dic_json[key]


json_txt(date_json)
print("dic ---: " + str(dic))
#value1 = ([(str(res(fanhuijson, key))) for key in result.keys()])