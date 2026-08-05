# Python with AI
## Lesson 2 - Variables and Data Types

---

# Learning Objectives

By the end of this lesson, students will be able to:

- Understand what variables are.
- Store and update data.
- Use different Python data types.
- Accept user input.
- Convert data between types.
- Build simple interactive programs.

---

# What is a Variable?

A variable is a container used to store information.

Think of a variable as a labeled box where you can keep data.

Example:

```python
name = "John"
```

Here:

- `name` is the variable.
- `"John"` is the value stored inside it.

---

# Creating Variables

```python
name = "Alice"
age = 20
country = "Somalia"

print(name)
print(age)
print(country)
```

Output

```
Alice
20
Somalia
```

---

# Variable Naming Rules

Good variable names:

```python
student_name = "Ali"
first_name = "Ahmed"
total_score = 90
```

Bad variable names:

```python
1name = "Ali"
my-name = "Ali"
class = "Python"
```

Rules:

- Start with a letter or underscore.
- Cannot start with a number.
- No spaces.
- Use meaningful names.
- Python keywords cannot be used.

---

# Updating Variables

Variables can change.

```python
score = 50

print(score)

score = 90

print(score)
```

Output

```
50
90
```

---

# Data Types

Python supports many data types.

The most common are:

| Data Type | Example |
|-----------|---------|
| String | `"Hello"` |
| Integer | `25` |
| Float | `3.14` |
| Boolean | `True` |

---

# Strings

Strings store text.

```python
language = "Python"

print(language)
```

Example

```python
first_name = "Ahmed"
last_name = "Ali"

print(first_name)
print(last_name)
```

---

# Integers

Integers are whole numbers.

```python
age = 21
students = 120

print(age)
print(students)
```

---

# Floats

Floats are decimal numbers.

```python
price = 10.99
height = 1.75

print(price)
print(height)
```

---

# Booleans

Booleans have only two values.

```python
True
False
```

Example

```python
is_student = True
has_license = False

print(is_student)
print(has_license)
```

---

# Checking Data Types

Use `type()`.

```python
name = "Ali"
age = 20
price = 15.5

print(type(name))
print(type(age))
print(type(price))
```

Output

```
<class 'str'>
<class 'int'>
<class 'float'>
```

---

# Getting User Input

Use `input()`.

```python
name = input("Enter your name: ")

print(name)
```

Example

```
Enter your name: Ahmed

Ahmed
```

---

# Multiple Inputs

```python
name = input("Name: ")
country = input("Country: ")

print(name)
print(country)
```

---

# Important Note

Everything entered using `input()` is stored as a string.

Example

```python
age = input("Age: ")

print(type(age))
```

Output

```
<class 'str'>
```

---

# Type Conversion

Convert a string into an integer.

```python
age = int(input("Age: "))

print(age)
```

Convert to float.

```python
price = float(input("Price: "))
```

Convert number to string.

```python
age = 20

text = str(age)

print(text)
```

---

# Example Program

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("You are", age, "years old.")
```

---

# Practice Examples

Example 1

```python
city = input("City: ")

print(city)
```

---

Example 2

```python
favorite_food = input("Favorite food: ")

print("You like", favorite_food)
```

---

Example 3

```python
number = int(input("Enter a number: "))

print(number)
```

---

# Exercises

## Exercise 1

Create a variable called `school`.

Print it.

---

## Exercise 2

Create variables for:

- name
- age
- country

Print all of them.

---

## Exercise 3

Ask the user for their favorite color.

Display it.

---

## Exercise 4

Ask the user for their age.

Print:

```
You are 20 years old.
```

---

## Exercise 5

Create two integer variables.

Print both.

---

## Exercise 6

Create two float variables.

Print both.

---

## Exercise 7

Create a boolean variable.

Print it.

---

## Exercise 8

Check the data type of:

- String
- Integer
- Float

---

## Exercise 9

Ask for the user's city.

Display a welcome message.

---

## Exercise 10

Ask for:

- Name
- Age
- Country

Print everything nicely.

---

## Exercise 11

Convert user input into an integer.

---

## Exercise 12

Convert user input into a float.

---

## Exercise 13

Convert an integer into a string.

---

## Exercise 14

Print your:

- Name
- Age
- Favorite Language
- Favorite Food

---

## Exercise 15

Create a simple student profile.

Example

```
Name: Ali
Age: 19
Country: Somalia
Course: Python
```

---

# Mini Challenge

Create a program that asks the user for:

- Name
- Age
- City
- Favorite Programming Language

Display the information in a clean format.

Example

```
===== Student Profile =====

Name : Ahmed
Age : 22
City : Hargeisa
Language : Python
```

---

# Homework

Create a file named

```
student_profile.py
```

Requirements:

The program should ask for:

- Full Name
- Age
- Country
- City
- University
- Favorite Programming Language

Then display everything in a professional format.

Example

```
=========================
      STUDENT PROFILE
=========================

Name       : Ahmed Ali
Age        : 22
Country    : Somalia
City       : Hargeisa
University : Example University
Language   : Python

Thank you for using our program!
```

---

# AI Prompt

Copy this prompt into ChatGPT.

---

I am learning Python Variables and Data Types.

Act as my Python mentor.

Do not write the full solution for me.

Explain each concept clearly using simple English.

After each explanation, give me one small exercise.

When I send my code:

- Review it carefully.
- Point out mistakes.
- Explain why they happened.
- Give hints instead of the complete answer.
- Encourage me to solve the problem myself.

At the end of the lesson, give me a small quiz with five questions.

---

# Lesson Summary

Today you learned:

✅ Variables

✅ Variable Naming Rules

✅ Strings

✅ Integers

✅ Floats

✅ Booleans

✅ type()

✅ input()

✅ Type Conversion

✅ Interactive Programs

Excellent work!

You are now ready to learn **Conditions and Loops** in Lesson 3.