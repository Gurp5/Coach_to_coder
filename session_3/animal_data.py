animals = [
 {"name": "capybara", "group": "mammal", "weight": 110},
 {"name": "hedgehog", "group": "mammal", "weight": 0.5},
 {"name": "bearded dragon", "group": "reptile", "weight": 1},
 {"name": "tortoise", "group": "reptile", "weight": 40},
 {"name": "hummingbird", "group": "bird", "weight": 0.01},
 {"name": "elephant", "group": "mammal", "weight": 10000},
 {"name": "ostrich", "group": "bird", "weight": 280},   
 {"name": "python", "group": "reptile", "weight": 180},
 {"name": "blue whale", "group": "mammal", "weight": 300000},
 {"name": "lion", "group": "mammal", "weight": 350}
]

# Let's consider the following tasks:
# 1. Print out all the animals names that are heavier than 100 pounds!
for animal in animals:
    if(animal["weight"] > 100):
        print(animal["name"])
# 2. Print out the heaviest animal!
previous_animal = 0 
for animal in animals:
    
    current_animal = animal["weight"]
    if(int(current_animal) > int(previous_animal)):
        previous_animal = current_animal
        animal_name = animal["name"]
        

print(f"The '{animal_name}' is the heaviest animal with a current weight of {previous_animal}")
# 3. Print out the lightest animal!

 
for animal in animals:

    current_animal = animal["weight"]
    
    
    if(current_animal < previous_animal):

       previous_animal = animal["weight"]
       animal_name = animal["name"]

print(f"The '{animal_name}' is the lightest animal with a current weight of {previous_animal}")
# 4. Print out all mammals as a list!

mammals = []

for animal in animals:
    if(animal["group"] == "mammal"):
        mammals.append(animal)
for mammal in mammals:
    print(mammal["name"])

# print out a list of animals with a name longer than 7 letters

animals_with_long_name = []

for animal in animals:
    if(len(animal["name"]) > 7):
        animals_with_long_name.append(animal)
print(animals_with_long_name)


