marks = {

    "Ayush": 98,
    "Akshat": 99,
    "Aaditya":95,
    
}

#print(marks.items())
#print(marks.keys())
#print(marks.values())
marks.update({"Ayush":97, "Gautam":100})
print(marks)

#print(marks.get("Ayush2"))   #prints None
#print(marks["Ayush2"])      #Return an error
