class Employee:
    company = "ITC"
    name= "Default Name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"out of all the languages here is your language: {self.language}")


#class Programmer:
#    company = "ITC Infotech"
#    def show(self):
#        print(f"The name is {self.name} and the salary is {self.salary}")
   
#    def showLanguage(self):
#        print(f"The name is {self.name} and he is goood with  {self.language} language")

class Programmer(Employee, coder):
    comapany = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is goood with  {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printlanguage()
b.showLanguage()