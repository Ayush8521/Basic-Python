'''
create a class "programmer" for storing information of few programers 
working at microsoft. '''

class Programmer:
    company = "Microsoft"
    def _init_(self,name,salary, pin,company):
        self.name = name
        self.salary = salary
        self.pin = pin
        self.company = company
        


p = Programmer("Ayush", 1200000, 201306, "Microsoft")
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", 1200000, 201306, "Microsoft")
print(r.name, r.salary, r.pin, r.company)
 
