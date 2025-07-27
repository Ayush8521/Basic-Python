s = {}
age= int(input("Enter your age: "))
status = "Adult"
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
s.update({"age": age, "status": status})
print(s)
