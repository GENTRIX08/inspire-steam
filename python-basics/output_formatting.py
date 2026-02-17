#Name : Gentrix Anyango
# Date : 17/02/2026
# Program to format the output in different styles

name = "Gentrix Anyango"

weight = 50 # weight in kgs

fav_team = "Liverpool"

height = 126.86 # height in cms

# 1. Format using printf(f"{}")

print(f"My name is {name} and I weigh {weight} in kgs")

# using f string
msg = f"My name is {name} and I support {fav_team}"
print(msg)

# 3 using {} and .format()
print("My name is{0} and I am {1} cms tall". format(name,height))

# 4 using output specifiers %s -strings

import math
print("The value of pi is approximately %5.3f")
print("I support %s" %fav_team)