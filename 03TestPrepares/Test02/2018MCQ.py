print(list(range(5)))

nums = [1,2,3]+[4,5,6]
print(nums)

friends = ["Aac", "Aab", "Aad"]

friends.pop()
print(friends)

a = "I,Am,A"
a.split(",")
print(a)

fruit = {"banana":1}
print(fruit.get("kiwi",0))
for item in fruit:
    print(item)

g = fruit.copy()
print(g)

ad = {"ww":1, "qq":2, "rr":3}
del ad["ww"]
print(ad)

ad["qq"] -= 1
print(ad)

print("qq" in ad)

print([0]*4)

nums = [3, 41, 12, 9, 74, 15]
print(max(nums))

food = {"pizza":3}
food["fries"] = 10
print(food)

treasure = {"gold":50, "silver":100}
print("gold" in treasure)

fortune = {"gold":500}
fortune["gold"] += 50
print(fortune)