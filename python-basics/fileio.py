#Name : Gentrix Anyango
# Date : 24/02/2026
# Program to perform file operations

# create new file 
new_file = open("student_data.txt","r+")


# write to new file
new_file.write("{ Student Name : Gentrix Anyango , ID : 3456789 , email:gentrix@gmail.com }")
new_file.close()



# read from the file
new_file = open("student_data.txt","r+")

data = new_file.read()

print(data)

new_file.close()


# delete file
# us os module
import os
os.remove("remove.txt")



# delete folder
os.rmdir("folder")




