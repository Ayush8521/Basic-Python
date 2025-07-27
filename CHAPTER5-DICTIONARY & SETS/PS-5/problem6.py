#create an empty dictionary.allow 4 friends to enter their favorite langusge as value and use key as their names.
#assume that the names are unique.

d = {}

name= input("Enter friends name: ")
lang= input("Enter friends favorite language: ")
d.update({name: lang})

name= input("Enter friends name: ")
lang= input("Enter friends favorite language: ")
d.update({name: lang})

name= input("Enter friends name: ")
lang= input("Enter friends favorite language: ")
d.update({name: lang})

name= input("Enter friends name: ")
lang= input("Enter friends favorite language: ")
d.update({name: lang})

print(d)