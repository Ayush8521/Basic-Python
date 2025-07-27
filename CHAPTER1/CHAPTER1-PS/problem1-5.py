import os
#select the directory whose content yuo want to list 
directory_path = '/'
#use the os module to list the directory content
entries = os.listdir(directory_path)

#print the content of the directory
for entry in entries:
    print(entry)
