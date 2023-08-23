# step by step procedure to solve a problem an end goal


# Setting up pin and balance

pin = 1234
balance = 50000
no_tries = 3

# prompting user for input
while no_tries > 0:
    input_pin = input("Please enter your PIN number!")


# turning input to int() so it can check for equality between 2 ints



    if(not input_pin.isdigit()):
        break

        if(pin == int(input_pin)):
        # turning balance to str so we can combine with message
            print("Your balance is " + str(balance))
            no_tries =0
        else:
            print("Incorrect PIN! Please try again!")
            no_tries = no_tries - 1