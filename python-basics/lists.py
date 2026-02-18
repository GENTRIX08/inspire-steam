#Name : Gentrix Anyango
# Date : 18/02/2026
# Program to show lists in python 

friends = ["Rachel","Phoebe","Chandler","Ross","Joey","Monica"]

print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)

friends.append("Jack")
print(friends)

new_friends = ["Tracy","James","Faith","Don","Augustine","Wendy"]

print(len(new_friends)) 

# new list of students
students = friends + new_friends
print(students)

print(students)
students.pop()
print(students)
students.insert(5,"Jenny")
print(students)
students.insert(9,"Valerie")
print(students)
students.extend("Dan")
print(students)

students.remove("Monica")
print(students)

new_students = students.copy()
print(new_students)