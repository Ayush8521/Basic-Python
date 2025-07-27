#WAP using function to find the greatest of three numbers.
def greatest_of_three_numbers(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 3
b = 2
c = 6
print("The greatest of three numbers is: ", greatest_of_three_numbers(a,b,c))
