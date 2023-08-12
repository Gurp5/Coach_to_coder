# we are not waiting for the user to input it but hard code the varibale
# change input variable to see both results

input_animal = "rabbit"

if input_animal == "rabbit":
    result = "nice one"
else:
    result= "thats not great"

print(result)

#or the above code could be simplified to the below:

result = "nice one" if input_animal == "rabbit" else "thats not great"

print(result)

# logical and and or operator

gurp_hungry = True
gurp_tired = True

if gurp_hungry == True and gurp_tired == True:
    print("leave him alone")
else:
    print("he is ok!")

#improve above

if gurp_hungry and gurp_tired:     
    print("leave him alone")
else:
    print("he is ok!") 

# or operator

if gurp_hungry or gurp_tired:
    print("he is tired or hungry or neither")
else:
    print("he is tired and hungry, give him space.")