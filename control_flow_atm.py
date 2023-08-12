
print("What is your 4 digit pin number please?")
result = input()
withdrawn = "withdraw"
deposit_amount = "deposit"
pin = 1234  
if int(result) == int(pin):
    balance = int(1000)
    string_balance = str(balance)
    print("Welcome to Bright Networks ATM your pin is correct and your balance is:" + " " + string_balance)
    print("would you like to withdraw or deposit some money?")
    result2 = input()
    if result2 == "withdraw":
        print("what is the amount you would like to withdraw from your account? please enter a sufficient amount or press 0 for nothing!")
        withdrawal1 = input()
        if int(withdrawal1) > int(0):
            balance = balance - int(withdrawal1)
        new_widthdraw_balance = str(balance)
        print("New balance ="  + " " + new_widthdraw_balance)
    if result2 == "deposit":
        print("how much money would you like to deposit to your account?")
        deposit = input()
        if int(deposit) > int(0):
            balance = int(balance)+int(deposit)
            new_balance = str(balance)
            print("Your updated balance is =" + " " + new_balance)
          
else:
    print("please try again! the pin entered is incorrect. Enter carefully as you have 2 more goes.")
    print("if all 3 attempts have been made your card will be blocked for security reasons.")
