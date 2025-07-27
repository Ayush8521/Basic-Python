class Employee:
    
    language = "python"  # this is a class attribute
    salary = 120000

    def getInfo(self):
         print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
         print("Good Morning")

rohan = Employee()
rohan.language = "Javascript" # This is an instance attribute
rohan.greet()
rohan.getInfo()
#Employee.getInfo(rohan)