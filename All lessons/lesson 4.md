# Python with AI
## Lesson 4 - Functions

---

# Learning Objectives

By the end of this lesson, students will be able to:

- Understand what functions are.
- Create functions using `def`.
- Use parameters and arguments.
- Return values using `return`.
- Understand local and global variables.
- Reuse code efficiently.
- Build simple calculator programs using functions.

---

# What is a Function?

A function is a block of reusable code.

Instead of writing the same code many times, we place it inside a function and call it whenever needed.

Example:

Without functions:

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

With functions:

```python
def greet():
    print("Welcome")

greet()
greet()
greet()
```

Output:

```
Welcome
Welcome
Welcome
```

---

# Why Use Functions?

Functions make code:

- Cleaner
- Shorter
- Easier to understand
- Reusable
- Easier to debug

Professional developers use functions in almost every project.

---

# Creating Your First Function

Syntax:

```python
def function_name():
    code
```

Example:

```python
def hello():
    print("Hello Python")

hello()
```

Output:

```
Hello Python
```

---

# Function Naming Rules

Good names:

```python
calculate_total()
show_menu()
print_student()
```

Bad names:

```python
x()
abc()
test1()
```

Use meaningful names.

---

# Parameters

Parameters allow functions to receive information.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Ahmed")
greet("Ali")
```

Output:

```
Hello Ahmed
Hello Ali
```

---

# Multiple Parameters

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Ali", 20)
```

---

# Arguments

Arguments are the values sent to functions.

Example:

```python
greet("Ahmed")
```

`"Ahmed"` is an argument.

---

# Returning Values

Functions can return values using `return`.

Example:

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

Output:

```
8
```

---

# More Return Examples

```python
def multiply(a, b):
    return a * b

answer = multiply(4, 6)

print(answer)
```

Output:

```
24
```

---

# Local Variables

Variables created inside functions are local.

Example:

```python
def test():
    name = "Ali"
    print(name)

test()
```

This works only inside the function.

---

# Global Variables

Example:

```python
school = "ABC School"

def show():
    print(school)

show()
```

Output:

```
ABC School
```

---

# Function with User Input

```python
def welcome():
    name = input("Enter name: ")

    print("Hello", name)

welcome()
```

---

# Example Calculator

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(10, 5))
print(subtract(10, 5))
```

---

# Example Area Program

```python
def area(length, width):
    return length * width

result = area(10, 5)

print(result)
```

Output:

```
50
```

---

# Default Parameters

Example:

```python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Ali")
```

Output:

```
Hello Student
Hello Ali
```

---

# Keyword Arguments

Example:

```python
def student(name, age):
    print(name)
    print(age)

student(age=20, name="Ahmed")
```

---

# Practice Examples

Example 1

```python
def welcome():
    print("Welcome to Python")

welcome()
```

---

Example 2

```python
def square(number):
    return number * number

print(square(5))
```

---

Example 3

```python
def is_adult(age):

    if age >= 18:
        return True
    else:
        return False

print(is_adult(20))
```

---

# Exercises

## Exercise 1

Create a function called:

```python
hello()
```

that prints:

```
Hello World
```

---

## Exercise 2

Create a function that prints your name.

---

## Exercise 3

Create a function with one parameter.

Example:

```python
greet(name)
```

---

## Exercise 4

Create a function that adds two numbers.

---

## Exercise 5

Create a function that subtracts two numbers.

---

## Exercise 6

Create a function that multiplies two numbers.

---

## Exercise 7

Create a function that divides two numbers.

---

## Exercise 8

Create a function that returns the square of a number.

---

## Exercise 9

Create a function that returns:

```python
True
```

if age is 18 or above.

---

## Exercise 10

Create a function that checks if a number is even.

---

## Exercise 11

Create a function that prints a multiplication table.

---

## Exercise 12

Create a function that displays student information.

Example:

```python
student(name, age, country)
```

---

## Exercise 13

Create a function that calculates rectangle area.

---

## Exercise 14

Create a function with default values.

---

## Exercise 15 (Challenge)

Create a menu function.

Example:

```
1. Add
2. View
3. Delete
4. Exit
```

---

# Mini Project

Build a Calculator using Functions.

Features:

- Addition
- Subtraction
- Multiplication
- Division

Example:

```
1. Add
2. Subtract
3. Multiply
4. Divide
```

User selects an option and enters numbers.

The program shows the result.

---

# Homework

Create a file:

```
calculator.py
```

Requirements:

- Use functions.
- Create:

```python
add()
subtract()
multiply()
divide()
```

- Show a menu.
- Allow users to perform calculations repeatedly.

---

# AI Prompt

Copy this prompt into ChatGPT.

---

I am learning Python Functions.

Act as my Python mentor.

Do not give me complete answers immediately.

Explain functions step by step.

When I write code:

- Review my code.
- Explain mistakes.
- Give hints.
- Suggest better function names.
- Show how professional programmers organize functions.

Help me improve my coding skills instead of simply generating solutions.

Finally, give me one beginner challenge, one intermediate challenge, and one advanced challenge.

---

# Lesson Summary

Today you learned:

✅ Functions

✅ def

✅ Parameters

✅ Arguments

✅ return

✅ Local Variables

✅ Global Variables

✅ Default Parameters

✅ Keyword Arguments

✅ Calculator Functions

🎉 Congratulations!

You have completed Lesson 4.

In Lesson 5, you will build a complete project:

**Student Management System**