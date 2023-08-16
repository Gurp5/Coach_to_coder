# 07_week_2_task 

rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]



total_river_length = 0

# 1. In a for loop, print out each river's name!
# 2. In another for loop, add up and print out the total length of all the rivers!

for river in rivers:
    river_name = river["name"]
    index = rivers.index(river)
    print(f"This is the {index}'st river:{river_name}")
    total_river_length += river["length"]
print(f"Total length of all rivers combined is: {total_river_length}")

# Extensions:
# 1. Print out every river's name that begins with the letter M !

letter = "M"


for river in rivers:
    if river["name"].startswith(letter):
        river_M = river["name"]
        print(f"The river '{river_M}' beigins with the letter 'M'")

# 2. The length of the rivers are in miles. Print out every river's length in kilometres! (1 mile is
# roughly 1.6 km)
    

for river in rivers:
     river_name = river["name"]
     river_length_miles = river["length"]
     print(f"river_name is {river_length_miles*1.6}km in length")

# Extra: create a sentance using the data provided in the list and dictionaries

for river in rivers:
    river_name = river["name"]
    river_length_miles = river["length"]
    print(f"The river {river_name} is a very nice river and is {river_length_miles}km long!")

