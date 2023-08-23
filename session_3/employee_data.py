employees = [
 {
 "first_name":"Jose",
 "last_name":"Lopez",
 "email":"joselopez0944@example.com",
 "age":25,
 "job_title":"Project Manager",
 "years_of_experience":1,
 "salary":8500,
 "department":"Product"
 },
 {
 "first_name":"Diane",
 "last_name":"Carter",
 "email":"dianecarter1228@example.com",
 "age":26,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":2,
 "salary":7000,
 "department":"Product"
 },
 {
 "first_name":"Shawn",
 "last_name":"Foster",
 "email": None,
 "age":37,
 "job_title":"Customer Service Rep",
 "years_of_experience":14,
 "salary":17000,
 "department":"Business"
 },
 {
 "first_name":"Brenda",
 "last_name":"Fisher",
 "email":"brendafisher3185@example.com",
 "age":31,
 "job_title":"Web Developer",
 "years_of_experience":8,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Sean",
 "last_name":"Hunter",
 "email": None,
 "age":35,
 "job_title":"Project Manager",
 "years_of_experience":11,
 "salary":14500,
 "department":"Product"
 },
 {
 "first_name":"Joshua",
 "last_name":"Jacobs",
 "email":"joshuajacobs5904@example.com",
 "age":28,
 "job_title":"Project Manager",
 "years_of_experience":3,
 "salary":10500,
 "department":"Business"
 },
 {
 "first_name":"Brianna",
 "last_name":"Marshall",
 "email":None,
 "age":33,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":10,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"John",
 "last_name":"Tate",
 "email":"johntate7881@example.com",
 "age":33,
 "job_title":"Mobile Developer",
 "years_of_experience":10,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"Jillian",
 "last_name":"Byrd",
 "email":None,
 "age":34,
 "job_title":"Business Analyst",
 "years_of_experience":10,
 "salary":11000,
 "department":"Business"
 },
 {
 "first_name":"Melanie",
 "last_name":"Sharp",
 "email":"melaniesharp9256@example.com",
 "age":41,
 "job_title":"Web Developer",
 "years_of_experience":15,
 "salary":14500,
 "department":"Product"
 },
 {
 "first_name":"Brandy",
 "last_name":"Mckee",
 "email":None,
 "age":37,
 "job_title":"Marketing Manager",
 "years_of_experience":14,
 "salary":14000,
 "department":"Business"
 },
 {
 "first_name":"Robert",
 "last_name":"Simpson",
 "email":"robertsimpson11778@example.com",
 "age":36,
 "job_title":"Marketing Manager",
 "years_of_experience":12,
 "salary":15000,
 "department":"Business"
 },
 {
 "first_name":"George",
 "last_name":"Mckenzie",
 "email":"georgemckenzie12384@example.com",
 "age":28,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":4,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Joseph",
 "last_name":"Smith",
 "email":None,
 "age":40,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":14,
 "salary":14000,
 "department":"Product"
 },
 {
 "first_name":"Dana",
 "last_name":"Crawford",
 "email":"danacrawford14310@example.com",
 "age":32,
 "job_title":"Project Manager",
 "years_of_experience":8,
 "salary":12000,
 "department":"Product"
 },
 {
 "first_name":"Christopher",
 "last_name":"Benson",
 "email":None,
 "age":29,
 "job_title":"Web Developer",
 "years_of_experience":5,
 "salary":7500,
 "department":"Product"
 },
 {
 "first_name":"Nicole",
 "last_name":"Smith",
 "email":"nicolesmith16360@example.com",
 "age":26,
 "job_title":"Designer",
 "years_of_experience":4,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Peter",
 "last_name":"Jimenez",
 "email":"peterjimenez17791@example.com",
 "age":28,
 "job_title":"UX Designer",
 "years_of_experience":3,
 "salary":6500,
 "department":"Business"
 },
 {
 "first_name":"Sergio",
 "last_name":"Boyle",
 "email":"sergioboyle18425@example.com",
 "age":31,
 "job_title":"Tester",
 "years_of_experience":6,
 "salary":9000,
 "department":"Product"
 },
 {
 "first_name":"Brianna",
 "last_name":"Moss",
 "email":None,
 "age":31,
 "job_title":"Designer",
 "years_of_experience":5,
 "salary":10500,
 "department":"Product"
 },
 {
 "first_name":"Taylor",
 "last_name":"Garner",
 "email":"taylorgarner20196@example.com",
 "age":32,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":6,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"Michael",
 "last_name":"Padilla",
 "email":"michaelpadilla21381@example.com",
 "age":29,
 "job_title":"Customer Service Rep",
 "years_of_experience":5,
 "salary":9500,
 "department":"Business"
 },
 {
 "first_name":"Yvette",
 "last_name":"Walker",
 "email":None,
 "age":26,
 "job_title":"Designer",
 "years_of_experience":2,
 "salary":7000,
 "department":"Product"
 },
 {
 "first_name":"Kristina",
 "last_name":"Pena",
 "email":"kristinapena23750@example.com",
 "age":34,
 "job_title":"Business Analyst",
 "years_of_experience":11,
 "salary":12500,
 "department":"Business"
 }
]
#1. Employee with the highest earning salary

previous_employees = 0

for employee in employees:
    if(previous_employees < employee["salary"]):
        previous_employees = employee["salary"]
        name = employee["first_name"]
print((f"The highest person earns {previous_employees} and there name is {name}"))

#2. Combined total number of the years of experince of each individual employee

employee_years = 0

for employee in employees:
    employee_years += employee["years_of_experience"]
year = int(employee_years)
print(f"The total number of comined years of experience within the company is {year} years!")

#3. Employees with no email with a 'none' key value data

employee_no_email = []

for employee in employees:
    if(employee["email"] == None):
        employee_no_email.append(employee["first_name"])

print(employee_no_email)

#4. The business department employee cost vs product department employee cost

business_cost = 0
product_cost = 0

for employee in employees:
    if(employee["department"] == "Business"):
        business_cost += employee["salary"]
    if(employee["department"] == "Product"):
        product_cost += employee["salary"]

if(business_cost > product_cost):
    print(f"The business department costs the business more in employee emuneration of {business_cost} than the product department costs of {product_cost}")
else:
    print(f"The product department costs the business more in employee emuneration of {product_cost} than the business department costs of {business_cost}")

# extension for thsiw weeks task

# 5. What is the average salary for people over 30 years of age?

combined_salary = 0 
no_employees =0 

for employee in employees:
    if(employee["age"] > 30):
        combined_salary += employee["salary"]
        no_employees += 1
average = combined_salary/no_employees
print(f"The average salary of the employees over the age of is: {int(average)}. What can we deduce from this? ")

# 6.  Create a new dict and calculate how many people are working with certain job titles. (HARD) Example: {"Project Manage": 4, "Machine Learning Engineer": 3, ...}


dicts = {"Machine Learning Engineer" : 0, "Customer Service Rep" : 0, "Web Developer" : 0, "Project Manager" : 0, "Mobile Developer" : 0, "Business Analyst" : 0, "Marketing Manager" : 0, "Designer" : 0, "UX Designer" : 0, "Tester" : 0}
listed = []

for employee in employees:
    listed.append(employee["job_title"])
        
for value in listed:
    if value in dicts:
       dicts[value] += 1

print(dicts)
print(listed)


