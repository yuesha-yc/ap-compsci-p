import itchat

itchat.login()
#爬取自己好友相关信息， 返回一个json文件，这里的friends是所有好友的jason信息
friends = itchat.get_friends(update=True)[0:]
#friends[0]是自己的信息
print(friends[0])

#初始化计数器
male = female = other = 0
#统计每一个好友的性别信息
for i in friends[1:]:
   # print(i['NickName'],i["Sex"])
    sex= i["Sex"]  #提取好友i的性别属性
    if sex==1:
        male+=1
    elif sex==2:
        female+=1
    else:
        other+=1
    
print(male,female,other,len(friends)-1)

