class Employee:
    def _init_(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def _init_(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def _init_(self):
        super()._init_()
        print("Constructor of Manager")
    c = 3

#o = Employee()
#print(o.a)   # prints the a attribute
#print(o.b)   #show an error as there is no b attribute in employee class


#o = Programmer()
#print(o.a,o.b)

o = Manager()
print(o.a,o.b, o.c)