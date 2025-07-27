a=int(input("Enter your age: "))
#If statement no. 1
if(a%2==0):
    print("you are entering an even number")
#end of If statement no. 1

#If statement no. 2
if(a>=18):
            print("you are above the age of consent")
            print("good for you")
elif(a<0):
           print("you are entering a invalid negative age")
elif(a==0):
           print("you are entering 0 which is not a valid age")
else:
        print("you are below the age of consent")

print("end of program")