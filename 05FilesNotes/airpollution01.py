# Print city name and pollution values for all cities with a pM 10 value of 20 or more
fhand = open("airpollution.txt")
for line in fhand:
    lien = line.rstrip()
    line = line.split(":")
    if int(line[1])>=20:
        print(line[0]+ " " +line[1])