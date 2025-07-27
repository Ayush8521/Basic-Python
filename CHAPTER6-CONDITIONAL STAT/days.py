days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days")
elif days > 7:
    print("Invalid number of days")
else:
    if days == 1:
        print("SUNDAY")
    elif days == 2:
        print("MONDAY")
    elif days == 3:
        print("TUESDAY")
    elif days == 4:
        print("WEDNESDAY")
    elif days == 5:
        print("THURSDAY")
    elif days == 6:
        print("FRIDAY") 
    elif days == 7:
        print("SATURDAY")
        