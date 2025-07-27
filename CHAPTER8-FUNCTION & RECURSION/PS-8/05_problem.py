#WAP function to calculate the sum of first n natural number.
'''
***
**        for n=3
*
'''  

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)


pattern(5)

   