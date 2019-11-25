#highest pm2.5 city and value
largestpm = 0
largestcity = ""
lowestpm = 9999
lowestcity = ""
total = 0
num = 0

fhand = open("airpollution.txt")
for line in fhand:
    lien = line.rstrip()
    line = line.split(":")
    if int(line[2]) > largestpm:
        largestpm = int(line[2])
        largestcity = line[0]
    if int(line[2]) < lowestpm:
        lowestpm = int(line[2])
        lowestcity = line[0]
    total += int(line[2])
    num += 1

print("Highest PM2.5: " + largestcity + " " + str(largestpm))
print("Lowest PM2.5: " + lowestcity + " " + str(lowestpm))
print("Average PM2.5: " + str(total/num))