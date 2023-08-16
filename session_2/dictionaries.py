# Dictionaries are objects in other objects for example

student = {
    "first_name": "Anna",
    "last_name" : "Henderson",
    "subject" : "Chemistry",
    "result" : 92,
    "contact_details": {
        "phone" : "1234",
        "email" : "anna@example.com"
    }
}
student["result"] = 99
student["date_of_birth"] = "24-07-1991"
print(student["first_name"])
print(student["date_of_birth"])
print("middle_name" in student)
print(student["result"])
print(student.keys())
print(student.values())

# print the phone number only
print(student["contact_details"]["phone"])

