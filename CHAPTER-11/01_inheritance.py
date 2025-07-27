class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


#class Programmer:
#    company = "ITC Infotech"
#    def show(self):
#        print(f"The name is {self.name} and the salary is {self.salary}")
   
#    def showLanguage(self):
#        print(f"The name is {self.name} and he is goood with  {self.language} language")

class Programmer(Employee):
    comapany = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is goood with  {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)