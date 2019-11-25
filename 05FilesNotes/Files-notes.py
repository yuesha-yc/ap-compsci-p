# Opening a file om read mode
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip() # remove the whitespaces
    if line.startswith("From:"): #
        print(line)

# Writing to a file
fout = open("datapump.txt", "w")
fout.write("Here is the lunch menu:\n")
food = "pizza, burgers, soda.\n"
fout.write(food)
fout.close()

readfile = open("datapump.txt")
for line in readfile:
    line = line.rstrip() # remove the whitespaces
    print(line)