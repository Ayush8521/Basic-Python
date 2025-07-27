f = open("file.txt")

#line = f.read1()
#print(line, type(line))


line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()
