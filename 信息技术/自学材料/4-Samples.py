import itchat, time
from itchat.content import *


import itchat

#将微信消息在控制台输出，并且回复
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
   print(msg['Text'])
   return " 你好，我是**的小助理，我主人正在上课，请下课之后联系，谢谢(#^.^#)"

itchat.auto_login(True)
itchat.run(True)

#将收到的信息类型以及内容，重新回复
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def reply(msg):
    msg.user.send( msg.type, msg.text)

#下载收到的图片、附件、视频等
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {PICTURE: 'img',VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


#通过好友添加请求，并发送nice to meet you 
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

#自动回复，某某已经收到信息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(msg.actualNickName, "received: ",  msg.text)

itchat.auto_login(True)
itchat.run(True)
