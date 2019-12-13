import itchat
import requests

apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
    'key':'',
    'info':'hello',
    'userid':'wechat-robot',
}
r = requests.post(apiUrl, data=data).json()
print(r)

#收到消息，直接回复
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg["Text"])
    if '我是' in msg['Text']:
        return msg['Text'][2:]+'，你好！'
    else:
        return ("hello")