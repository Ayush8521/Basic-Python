class Employee:
    
    language = "python"  # this is a class attribute
    salary = 120000


rohan = Employee()
#rohan.language = "Javascript" # This is an instance attribute
print(rohan.salary,rohan.language)