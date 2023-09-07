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
# 2. A bar chart showing the average mileage for each model. (You need to research how
# can you calculate average using pandas!)

Car = namedtuple("car", "model, year, price, transmission, mileage, fuel_Type, tax, mpg, engine_Size")

with open("vw.csv", "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    cars = [Car(*row) for row in reader]

# Question 1: What is the most expensive VW car listed?

most_expensive_car = cars[0]
for car in cars:
    if(int(car.price) > int(most_expensive_car.price)):
        most_expensive_car = car
print(f"Question 1 - The most expensive model is the '{most_expensive_car.model}'")

# Question 2: Find all the VW Golf models. What is their average price?

car_total_values = 0
no_golf_models = 0
for car in cars:
    if(car.model == "Golf"):
        no_golf_models += 1
        car_total_values += int(car.price)
# print(no_golf_models)
# print(car_total_values)
Ave = car_total_values/no_golf_models
print(f"Question 2 - The average price of the VW Golf model is £{Ave}")

# Question 3: What is the average milage for VW Polo models registered in 2020?

# car_total_values1 = 0
# no_golf_models1 = 0
# for car in cars:
#     if(car.model == "Golf" and car.year == 2020):
#         no_golf_models1 += 1
#         car_total_values1 += float(car.mileage)
# print(no_golf_models1)
# print(car_total_values1)

# List comprehension way

car_total_values1 = 0
no_golf_models1 = 0
total_miles = 0
Average_miles = 0

Average_miles = [car for car in cars if int(car.year) == 2020 and car.model == "Polo"]

list_len = len(Average_miles)
total_miles += int(car.mileage)
Ave_miles = total_miles/list_len

print(f"Question 3 - The average mileage for the VW Polo model is {Ave_miles}")

# print(Average_miles)

# Extension: Using pandas and matplotlib , create the following:
# 1. A pie chart showing the distribution between fuel types. (You can use the model column to count occurances!)
# 2. A bar chart showing the average mileage for each model. (You need to research hpow can you calculate average using pandas!)

# Ex - Question 1

fuel_types_dis = [car for car in cars]


with open("vehicle_analysis_data.csv", "w") as vw_csvfile:
    writer =  csv.writer(vw_csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(Car("model", "year", "price", "transmission", "mileage", "fuel_Type", "tax", "mpg", "engine_Size"))
    for car in cars:
        writer.writerow(car)

# Ex - Question 2