#Name : Gentrix Anyango
# Date : 19/02/2026
# Program to show classes in python

class Car():
    # Attributes of the car

    def __init__(self,model,make,colour,year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year

    # print car details
    def print_details(self,model,make,colour,year):
         print(f"{make} {model} of colour {colour} was manufactured in the year {year}")
    
    
#instantiate a class object

my_car = Car("Atenza","Bugatti","Black", "2020")
dads_car = Car("Mitsubishi","subaru","red", "2023")

my_car.print_details("Atenza","Bugatti","Black","2020")
my_car.print_details("Mitsubishi","subaru","red","2023")
   
   