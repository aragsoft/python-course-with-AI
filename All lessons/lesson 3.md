# Python with AI
## Lesson 3 - Conditions and Loops

---

# Learning Objectives

By the end of this lesson, students will be able to:

- Understand conditional statements.
- Make decisions using `if`, `elif`, and `else`.
- Compare values using comparison operators.
- Use logical operators.
- Repeat tasks using loops.
- Write simple decision-making programs.

---

# What are Conditions?

Conditions allow a program to make decisions.

Example:

If a student passes the exam, print **"Congratulations!"**

Otherwise, print **"Try Again."**

Programs become more useful when they can make decisions.

---

# The if Statement

Syntax:

```python
if condition:
    # code
```

Example

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

Output

```
You are an adult.
```

---

# if and else

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```
Minor
```

---

# if, elif, else

Use `elif` when there are multiple conditions.

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Need More Practice")
```

Output

```
Grade B
```

---

# Indentation

Python uses indentation instead of braces.

Correct

```python
if True:
    print("Hello")
```

Wrong

```python
if True:
print("Hello")
```

Always use **4 spaces** for indentation.

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

Example

```python
age = 20

print(age > 18)
```

Output

```
True
```

---

# Equality

```python
password = "python123"

if password == "python123":
    print("Access Granted")
```

---

# Not Equal

```python
name = "Ali"

if name != "Ahmed":
    print("Different Name")
```

---

# Logical Operators

Python provides three logical operators.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses a condition |

---

# Using and

```python
age = 22
country = "Somalia"

if age >= 18 and country == "Somalia":
    print("Eligible")
```

---

# Using or

```python
role = "Teacher"

if role == "Teacher" or role == "Admin":
    print("Access Granted")
```

---

# Using not

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

---

# Nested if

```python
age = 25

if age >= 18:

    license = True

    if license:
        print("You can drive.")
```

---

# Introduction to Loops

Loops repeat code automatically.

Without loops:

```python
print("Python")
print("Python")
print("Python")
```

With loops:

```python
for i in range(3):
    print("Python")
```

---

# The for Loop

Syntax

```python
for variable in range(number):
    code
```

Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# range()

Examples

```python
range(5)
```

Produces

```
0 1 2 3 4
```

---

```python
for i in range(1,6):
    print(i)
```

Output

```
1
2
3
4
5
```

---

# Counting Backwards

```python
for i in range(5,0,-1):
    print(i)
```

Output

```
5
4
3
2
1
```

---

# while Loop

A `while` loop runs as long as the condition is True.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

# Infinite Loop

Wrong

```python
while True:
    print("Hello")
```

This loop never stops.

Always make sure your condition eventually becomes False.

---

# Loop with User Input

```python
number = int(input("Enter a number: "))

for i in range(number):
    print("Python")
```

---

# Example Program

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Welcome")
else:
    print("Access Denied")
```

---

# Example Login Program

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")
```

---

# Practice Examples

Example 1

```python
temperature = 35

if temperature > 30:
    print("Hot")
```

---

Example 2

```python
for i in range(10):
    print(i)
```

---

Example 3

```python
count = 1

while count <= 3:
    print("Welcome")
    count += 1
```

---

# Exercises

## Exercise 1

Check whether a number is positive or negative.

---

## Exercise 2

Ask the user for their age.

Print:

```
Adult
```

or

```
Minor
```

---

## Exercise 3

Check whether a number is even or odd.

(Hint: `%` operator)

---

## Exercise 4

Create a grading system.

90+

```
A
```

80+

```
B
```

70+

```
C
```

Below 70

```
Fail
```

---

## Exercise 5

Ask the user for a password.

If it matches:

```
Welcome
```

Otherwise:

```
Incorrect Password
```

---

## Exercise 6

Print numbers from 1 to 20.

---

## Exercise 7

Print only even numbers from 2 to 20.

---

## Exercise 8

Print numbers from 20 down to 1.

---

## Exercise 9

Use a while loop to print:

```
Hello
```

five times.

---

## Exercise 10

Ask the user for a number.

Print its multiplication table.

Example

```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## Exercise 11

Count how many numbers from 1–100 are divisible by 5.

---

## Exercise 12

Ask for username and password.

Allow login only if both are correct.

---

## Exercise 13

Ask the user to enter a number.

Print every number from 1 up to that number.

---

## Exercise 14

Print all odd numbers from 1 to 50.

---

## Exercise 15 (Challenge)

Build a simple menu.

```
1. Start

2. Help

3. Exit
```

If the user enters:

```
1
```

Print

```
Program Started
```

If

```
2
```

Print

```
Help Center
```

If

```
3
```

Print

```
Goodbye
```

Otherwise

```
Invalid Choice
```

---

# Homework

Create a file called

```
login_system.py
```

Requirements

- Ask for username.
- Ask for password.
- If username is `admin` and password is `python123`
  display:

```
Login Successful
```

Otherwise display:

```
Access Denied
```

After a successful login, display:

```
===== MENU =====

1. Profile
2. Settings
3. Logout
```

---

# AI Prompt

Copy this prompt into ChatGPT.

---

I am learning Python Conditions and Loops.

Act as my Python instructor.

Do not write the complete solution for me.

Explain every concept using simple examples.

After each explanation, give me one practice exercise.

When I submit my code:

- Review it line by line.
- Explain any mistakes.
- Give hints instead of the full answer.
- Suggest a better way if my solution works but can be improved.

Finally, give me three coding challenges that become progressively harder.

---

# Lesson Summary

Today you learned:

✅ if

✅ elif

✅ else

✅ Comparison Operators

✅ Logical Operators

✅ Nested Conditions

✅ for Loop

✅ while Loop

✅ range()

✅ Simple Login Programs

✅ Decision Making

🎉 Congratulations!

You have completed Lesson 3.

In **Lesson 4**, you will learn **Functions**, one of the most powerful features in Python that helps you write clean, reusable, and professional code.