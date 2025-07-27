class Employee:
    language = "python"  # this is a class attribute
    salary = 120000

Ayush = Employee()
Ayush.name = "Ayusch"   # This is an instance attribute
print(Ayush.name,Ayush.language,Ayush.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary,rohan.language)

#  Here name is instance attribute and salary and language are class attributes as they directly belong
# to the class.