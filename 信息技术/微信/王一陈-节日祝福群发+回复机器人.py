import itchat
import requests
import datetime

itchat.login()
# 爬取自己好友相关信息， 返回一个json文件，这里的friends是所有好友的jason信息
friends = itchat.get_friends(update=True)



switch = input("输入'开始群发'开始节日祝福")
if switch == "开始群发":
    strTime = datetime.datetime.now().strftime("%m%d")
    if strTime[0:1] == "12" and strTime[2:3] == "25":
        holiday = "圣诞节🎄"
    elif strTime[0:1] == "01" and strTime[2:3] == "01":
        holiday = "新年"
    elif strTime[0:1] == "05" and strTime[2:3] == "01":
        holiday = "劳动节"
    elif strTime[0:1] == "06" and strTime[2:3] == "01":
        holiday = "儿童节"
    elif strTime[0:1] == "07" and strTime[2:3] == "01":
        holiday = "建党节"
    elif strTime[0:1] == "01" and strTime[2:3] == "01":
        holiday = "建军节"
    elif strTime[0:1] == "09" and strTime[2:3] == "01":
        holiday = "开学节"
    elif strTime[0:1] == "10" and strTime[2:3] == "01":
        holiday = "国庆节"
    elif strTime[0:1] == "11" and strTime[2:3] == "11":
        holiday = "双十一，你买东西了吗，"
    elif strTime[0:1] == "10" and strTime[2:3] == "31":
        holiday = "万圣节"
    elif strTime[0:1] == "12" and strTime[2:3] == "31":
        holiday = "狂欢节"
    else:
        holiday = "平常的一天"
    for i in friends[0:1]:
        print(i)
        print(type(i))
        sex = i["Sex"]  # 提取好友i的性别属性
        username = i["UserName"]# UUID
        nickname = i["NickName"]
        province = i["Province"]
        city = i["City"]
        if sex == 1:
            itchat.send_msg("身在" + province + city + "的男性朋友，" + nickname + "今天是" + holiday +  " ，祝你节日快乐！", toUserName=None)
        else:
            itchat.send_msg("身在" + province + city + "的女性朋友，" + nickname + "今天是" + holiday +  " ，祝你节日快乐！", toUserName=None)

# 小助手
from itchat.content import *

MyName = friends[0]["NickName"]
@itchat.msg_register(TEXT, PICTURE, VIDEO, ATTACHMENT)
def replyservant(msg):
    if '我是' in msg['Text']:
        return msg['Text'][2:]+'，你好！'
    else:
        return ("你好，我是" + MyName + "的AI小助手！")

@itchat.msg_register(TEXT, PICTURE, VIDEO, ATTACHMENT)
def downloadfiles(msg):
    msg.download(msg['Filename'])
    filename = str(msg['Filename'])
    itchat.send_msg(MyName + "的AI助手已经收到了您发送的文件：" + filename + "请您放心！", toUserName=msg['FromUserName'])

@itchat.msg_register(TEXT, PICTURE, VIDEO, ATTACHMENT)
def downloadpic(msg):
    msg.download(msg['Text'])
    picname = str(msg['Text'])
    itchat.send_msg(MyName + "的AI助手已经收到了您发送的文件：" + picname + "请您放心！", toUserName=msg['FromUserName'])

@itchat.msg_register(TEXT, PICTURE, VIDEO, ATTACHMENT)
def downloadvideo(msg):
    msg.download(msg['Text'])
    videoname = str(msg['Text'])
    itchat.send_msg(MyName + "的AI助手已经收到了您发送的文件：" + videoname + "请您放心！", toUserName=msg['FromUserName'])