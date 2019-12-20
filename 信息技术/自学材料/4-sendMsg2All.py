#群发助手
import itchat

itchat.login()

#想给指定的人发消息
users=itchat.search_friends("SXC")
userName= users[0]['UserName']
print(userName)
itchat.send('你好！我是韩老师的微信机器人',toUserName=userName)


#群发消息
friends = itchat.get_friends(update=True)[0:]
#friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
   if i['Sex']==1:
      itchat.send(i['RemarkName']+",圣诞快乐！"，toUserName=i['UserName'] )
      #itchat.send('我是**的聊天机器人，你好呀！'+i['UserName'],toUserName=i['UserName'])
