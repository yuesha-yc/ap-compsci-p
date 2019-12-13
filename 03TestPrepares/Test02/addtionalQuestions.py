# 4 Login
database = {"Jack":1234, "Henry":3251, "Kevin":1716, "Simpson":2579, "Michael":7658}
username = input("Please enter your user name and passwords!\n")
password = int(input())
if username not in database.keys():
    print("Invalid username!")
else:
    if password != database[username]:
        #print(database[username])
        print("Invalid password!")
    else:
        print("Login successful!")

# 5 Team Win-Lose
database = {}
for i in range(1,2):
    win_lost = []
    team = input("Enter the name of the team: \n")
    wins = int(input("Enter the number of wins: \n"))
    losts = int(input("Enter the number of losts: \n"))
    win_lost.append(wins)
    win_lost.append(losts)
    #print(win_lost)
    database[team] = win_lost
    #print(database)

# a)
request = input("Enter a team name for percentage: \n")
percentage = (database[request][0]/(database[request][0] + database[request][1]))*100
print("%" + str(percentage))

# b)
winning = []
for list in database.values():
    winning.append(list[0])
print(winning)