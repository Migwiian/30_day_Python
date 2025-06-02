print('Hello World')  # String
# Built-in functions in Python  
len('Hello World') # Returns the length of the string   
type('Hello World') # Returns the type of the string
str(39) # Converts the integer 39 to a string
int('39') # Converts string to integer  
float('39') # Converts string to float
bool(1) # Converts 1 to boolean, returns True
bool(0) # Converts 0 to boolean, returns False
input('Enter your name: ') # Takes input from the user
abs(-10) # Returns the absolute value of -10, which is 10
round(3.14) # Rounds 3.14 to the nearest integer, which is 3
max(1, 2, 3) # Returns the maximum value among the arguments, which is 3
min(1, 2, 3) # Returns the minimum value among the arguments, which is 1
sum([1, 2, 3]) # Returns the sum of the list elements, which is 6
sorted([3, 1, 2]) # Returns a sorted list, which is [1, 2, 3]
sorted([3, 1, 2], reverse=True) # Returns a sorted list in descending order, which is [3, 2, 1]
list('Hello') # Converts the string 'Hello' to a list of characters, which is ['H', 'e', 'l', 'l', 'o']
dict(name='Asabeneh', age=250) # Creates a dictionary with keys 'name' and 'age'
set([1, 2, 2, 3]) # Converts the list to a set, which removes duplicates, resulting in {1, 2, 3}
tuple([1, 2, 3]) # Converts the list to a tuple, which is (1, 2, 3)
range(5) # Creates a range object from 0 to 4
range(1, 6) # Creates a range object from 1 to 5
range(1, 10, 2) # Creates a range object from 1 to 9 with a step of 2
#variables in python
first_name='Ian'
country='Kenya'
town='Nyeri'
age=27
is_married=False
skills=['Python', 'mySQL', 'Excel']
person_info={
    'first_name': first_name,
    'country': country,
    'town': town,
    'age': age,
    'is_married': is_married,
    'skills': skills
}
print(person_info)
first_name, country, town, age, is_married, skills = 'Ian', 'Kenya', 'Nyeri', 27, False, ['Python', 'mySQL', 'Excel']
print(first_name, country, town, age, is_married, skills)
# Multiple assignment
x, y, z = 5, 10, 15
print(x, y, z)  # Output: 5 10 15
# Swapping variables
a, b = 1, 2
print(a, b)  # Output: 1 2
a, b = b, a
print(a, b)  # Output: 2 1
# Using built-in functions with variables
name = 'Ian'
length_of_name = len(name)  # Length of the string 'Ian'
print(length_of_name)  # Output: 3
