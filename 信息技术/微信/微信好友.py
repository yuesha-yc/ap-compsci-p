import itchat

itchat.login()

friends = itchat.get_friends(update=True)[0:]
print(friends[0])

beijing = 0
others = 0
for i in friends[1:]:
    province = i["Province"]
    if province == "北京":
        beijing += 1
    else:
        others += 1

print(beijing,others)
