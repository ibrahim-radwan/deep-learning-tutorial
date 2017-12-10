# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:05:23 2017

@author: Ibrahim Radwan
"""

print("Hello!")

# Variables, cannot start with numbers
# strings
greeting = "Hello!"
print(greeting)

# get the value of the variable from the user:
greeting = input("Please enter a greeting: ")
print(greeting)

# numbers
a = 2
b = 5
print(a+b)

age = input("Please enter your age: ")
print("Your age is: ", age)
#new_age = age + 50 # TypeError: must be str, not ints
new_age = int(age) + 50 
print("Your new age is: ", new_age)

"""
Please create two variables namely name  and age and assign values "Ibrahim Radwan"
and 33 respectively. Don't forget that everything in Python is case sensitive. 
"""

"""
1. Create a variable named price and assign it a value of 10 .
2. Print out the value of variable price .
"""

# Numbers and operators
num = 20 - 10 / 5 * 3 ** 2 # order of operations (exp is first)
print(num)

num = (20 - 10) / 5 * 3 ** 2 # order of operations (brackets are first)
print(num)

num = (20 - 10) / (5 * 3) ** 2 # order of operations (brackets are first)
print(num)

# Strings
c = "Here"
c = c.replace("e", "i")
print(c)
c = c.upper()
print(c)
print(c + " There")

# String indexing and splitting
c = "Hi There!"
print(c[3])
type(c[2])
print(c[8])
print(c[-1])
print(c[0:1])
print(c[0:3])
print(c[:3])
print(c[3:])

# ex
letters = 'abcdefghijklmnopqrstuvwxyz'
#print(letters[-2:]) Fill in the empty square brackets so that the script prints out 'xy' .
#print(letters[-3:-1])
