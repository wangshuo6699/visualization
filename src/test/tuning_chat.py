import json
import urllib.request

api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = input('我：')
# text_input = '你好'

req = {
    "perception":
    {
        "inputText":
        {
            "text": text_input
        },

        "selfInfo":
        {
            "location":
            {
                "city": "禹州",
                "province": "河南省",
                "street": "泰山庙街"
            }
        }
    },

    "userInfo":
    {
        # "apiKey": "e02192acc9d947b8b149d3e929514f6f",
        "apiKey": "98f95153fb5c4684a5602b909949ba61",
        "userId": "OnlyUseAlphabet"
    }
}
# print(req)
# 将字典格式的req编码为utf8
req = json.dumps(req).encode('utf8')
# print(req)

http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(http_post)
response_str = response.read().decode('utf8')
response_dic = json.loads(response_str)

intent_code = response_dic['intent']['code']
results_text = response_dic['results'][0]['values']['text']
print('Turing的回答：')
print('code：' + str(intent_code))
print('text：' + results_text)
