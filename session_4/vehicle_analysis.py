import csv 
from collections import namedtuple

# Week 4 Task

# Base task: Using the csv package, read in the data from the vw.csv file, and turn
# them into a list of dicts or a list of namedtuples, similar to how we did things for the Amazon
# bestseller list during the lesson. Answer the following questions:

# 1. What is the most expensive VW car listed?
# 2. Find all the VW Golf models. What is their average price?
# 3. What is the average milage for VW Polo models registered in 2020?
# Extension: Using pandas and matplotlib , create the following:
# 1. A pie chart showing the distribution between fuel types. (You can use the model column
# to count occurances!)
# 2. A bar chart showing the average mileage for each model. (You need to research hpow
# can you calculate average using pandas!)

Car = namedtuple("car", "model, year, price, transmission, mileage, fuel_Type, tax, mpg, engine_Size")

with open("vw.csv", "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    cars = [Car(*row) for row in reader]

# Question 1: What is the most expensive VW car listed?

most_expensive_car = cars[0]
for car in  cars:
    if(int(car.price) > int(most_expensive_car.price)):
        most_expensive_car = car
print(most_expensive_car)

# 2. Find all the VW Golf models. What is their average price?

car_price = cars[3]
car_total_values = 0
for car in  cars:
    if(car.model == "Golf"):
        car_total_values+= car_total_values
print(car_total_values)