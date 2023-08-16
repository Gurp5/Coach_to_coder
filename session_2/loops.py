balance = 500

pin_number = 1234

input_pin = int(input("Enter your pin number please:"))

while(input_pin != pin_number):
    print("Wrong number, please try again!")
    input_pin = int(input())

print(f"Your balance is £{balance}")