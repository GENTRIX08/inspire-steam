#Name : Gentrix Anyango
# Date : 13/02/2026
# Program to calculate geometric progression

# calculating nth term

a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
r = int(input("Enter the common ratio :"))

nth_term = a * (r ** (n-1))
print(f"The nth term is : {nth_term} ")
