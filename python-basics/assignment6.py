#Name : Gentrix Anyango
# Date : 17/02/2026
# Program to display diamond and triangle

n = 4 # height of diamond

# Top part
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Bottom part
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

n = 5 # height of triangle

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(f"\nQuadratic equation: {a}x^2 + {b}x + {c} = 0")

d =
