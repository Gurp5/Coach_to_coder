# we use the variable 'number' to store each number appose to make 5 variables for each number/data in the list.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# total = 0

# # for number in numbers:
# #     if(number != 2):
# #         total += number
# # print(total)

# combine dictionaries into a list 

students = [
    {"name": "Anna", "result": 92},
    {"name": "James", "result": 98},
    {"name": "Graham", "result": 88},
    {"name": "Davis", "result": 67},



]

average = 0
for student in students:
    average += student["result"]
mean = average/len(students)
print(mean)
    



