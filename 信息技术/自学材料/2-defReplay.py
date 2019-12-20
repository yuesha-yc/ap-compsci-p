import itchat

#根据收到消息的内容，自定义不同回复
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
   print(msg['Text'])
   if '我是' in msg['Text'] :
      return msg['Text'][2:]+",你好,!" +'我主人在忙，请稍后联系！(#^.^#)'
   elif msg['Text'] in ['你好','您好','hello','hi']:
      return "你好~ 请问你是谁？"
   else:
      return "我是韩老师的AI小助理，我主人正忙，稍后回复您！谢谢♪(･ω･)ﾉ"
   
itchat.auto_login(True)
itchat.run(True)
