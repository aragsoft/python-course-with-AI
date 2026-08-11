# if,  else
age =15
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# if, elif, else
score = 90
if score < 90:
    print("A")
elif score < 80:
    print("B")
elif score < 70:
    print("C")
else:
    print("D")



# if statement with comparison operators
name = "Ali"

if name != "ahmed":
    print("Different Name")


# if statement with comparison operators
age = 12
country = "Somalia"

if age >= 18 and country == "Somalia":
    print("Eligible") 
# else:
#     print("Not Eligible")   



# if statement logical operators
role = "amixiid"

if role == "Teacher" or role == "Admin":
    print("Access Granted")





# if statement with logical operators
logged_in = True

if not logged_in:
    print("Please Login")    

    
# nested if statements
age = 25

if age >= 18:

    license = False

    if license:
        print("You can drive.")



# for loop
for i in range(10):
    print("python")

# backward for loop
for i in range(5,0,-1):
    print(i)


# while loop
count = 1

while count <= 5:
    print(count)
    count += 1



# infinite loop

# while True:
#     print("Hello")

# for loop with user input
number = int(input("Enter a number: "))

for i in range(number):
    print("Python")

    



# login program

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")
