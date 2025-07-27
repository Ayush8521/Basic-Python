'''
WAP to generate multiplication table from 2 to 20 and write it to the 
the different files. place these files in a folder for a 13-year old.
'''

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables_{n}.txt", "w") as f:
        f.write(table)

for i in range(2,20):
    generateTable(i)