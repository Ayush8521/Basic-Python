a=(1,45,342,3424,False,"rohan","AYUSH")
print(a)

no = a.count(45)
print(no)
#a= (10, 20, 30, 40)
#print(a.index(30))  # Output: 2

i = a.index(3424)
print(i)

#concatenation:

tuple1 = (1,2,3)
tuple2 = (4,5,6)

concatenated = tuple1 + tuple2
print(concatenated)        #concatenetation
print(len(concatenated))   #length of tuple
print(5 in concatenated)   #Membership Test (in)

t = (1,2)*3  #Repetation(*)
print(t)


t = ('a', 'b', 'c')
for item in t:
    print(item)
