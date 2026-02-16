#Name : Gentrix Anyango
# Date : 16/02/2026
# Program to calculate factorials of numbers

factorial = 1 #initialize factorial
number = int(input("Enter the number x: "))

for x in range(1,number + 1):
    factorial *= x
    

print(f"{number}! = {factorial}")    