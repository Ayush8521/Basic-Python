class Employee:
    
    language = "python"  # this is a class attribute
    salary = 120000


    def _init__(self,name,salary,language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
     print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
         print("Good Morning")

rohan = Employee("Rohan", 1300000, "Javascript")
#rohan.name = "Rohan" 
print(rohan.name, rohan.salary, rohan.language)
#rohan._init__()

rohan.Employee()

