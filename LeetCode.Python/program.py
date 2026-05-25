nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
print(squared)

# this is single line comment
"""
this is a multi-line string.
"""

print("Python tour - let's go")

# === 1. Numbers ===

print("-- numbers --")
a = 42
b = 3.15
big = 2 ** 100
print(a, b, big)
print (10 / 3)
print(10 // 3)
print(10 % 3)
print(-7 // 2)

n = 10
n += 5; n -= 2; n *= 3; n //= 4
print(n)
# no ++ or -- operators in Python

# === 2. Strings ===

print("-- strings --")
s1 = 'single quotes'
s2 = "double quotes"
s3 = """ ultil
liine 
string
"""
# string is immutable
print("hi" + "Bo" + s1)
print(s1[2])
print("abcdefg"[2:5])
print("abcdefg"[:4])
print("abcdefg"[:-1])
print("abcdefg"[::-1])

# f-string - Python's interpolated strings
age = 7
print(f"my age is {age} years, {age * 12} months")
print(f"{3.1515926:.2f}")
print(f"{12312341:.2e}")

# string common methods, retrun new string, original unchanged becase immutable
s = " Hello, World!  "
print(s.strip())
print(s.lower())
print(s.replace("World", "Python"))
print("a,b,c".split(","))
print(",".join(["a", "b", "c"]))

# Conversion
print(int("42") + 1)
print(str(333) + " is a number")
print(float("3.14"))


# === 3.Booleans + None ===

print("-- booleans and None --")

# True, False, None are special constants in Python, no ! in Python, use not instead
t = True
f = False
n = None
print(True and False)
print(True or False)
print(not True)
print(None)
print(not None)
print(not not None)

#Truthness - they are all False:
# False, Node, 0, 0.0, "", [], {}, set(), and other empty collections
# everything else is True
nums = [0, 1, 2, 3]
if nums:
    print("nums is not empty")
print(0 or "fallback")
print(0 and "fallback")
print("a" and "b") # returns the last value if all are true, otherwise returns the first false value
print(0 and "b")
print("a" and 0 or "b")
print("a" and 0 and "b")

# === 4. Variables + Assignment ===

print("-- variables and assignment --")

# No type declaration, dynamic typing
x = 10
x = "Bo Li"
x = [1, 2, 3]
x = [1, "two", 3.0, [4, 5]]

a, b = 1, 2
print(a, b)
a ,b = b, a
print(a, b)
first, second = [1, 2]
print(first, second)
# * operator can be used to unpack the rest of the values into a list
first, second, *rest = [1, 2, 3, 4, 5]
print(first, second, rest)
*init, last = [1, 2, 3, 4, 5]
print(init, last)
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)
# walrus operator - assign and return a value in the same expression
nums = [1, 2, 3, 4, 5]
# can't do n := len(nums) in the condition of an if statement, but can do it with walrus operator
if (n := len(nums)) > 3:
    print(f"nums has {n} elements, which is more than 3")

# === 5. List ===

print("-- lists --")

nums = [3, 1, 4, 1, 5]
emty = []
zeros = [0] * 5
grid = [[0] * 3 for _ in range(3)]
print(nums, emty, zeros, grid)
# conprehension
numsc = [x ** 2 for x in range(10) if x % 2 == 1]
print(numsc)
numsc = [x ** 2 if x % 2 == 1 else x ** 3 for x in range(10)]
print(numsc)
numsc = [x ** 2 for x in range(10) if x % 2 == 1 if x > 5]
print(numsc)
nums = [x * 2 for x in range(10) for _ in range(3)]
print(nums)

# Properties
print(len(nums)) # length of the list
print(3 in nums) # membership test
print(nums[0]) # indexing
print(nums[-1]) # last element

# Slicing
# nums[start: stop: step] start is inclusive, stop is exclusive, step can be negative for reverse
print(nums[1:5]) # from index 1 to 4
print(nums[:5]) # from start to index 4
print(nums[5:]) # from index 5 to end
print(nums[::2]) # every other element
print(nums[::-1]) # reverse the list
print(nums[-2:-5:-1]) # from index 5 to 2 in reverse

# Mutation - modifies in places
xs = [3, 1, 4, 1, 5]
xs.append(9) # add an element to the end of the list
xs.insert(2, 2) # insert an element at a specific index
xs.pop() # remove and return the last element
xs.pop(0) # remove and return the element from begin, O(n) time complexity
xs.remove(1) # remove the first occurrence of a value, O(n) time complexity, raises ValueError if the value is not found
xs.extend([6, 5, 3]) # add multiple elements to the end of the list, like AddRange in C#
xs += [6, 5, 3] # same as extend
xs *= 2 # repeat the list multiple times
print(xs)
xs.sort() # sort the list in place, O(n log n) time complexity
print(xs)
xs.reverse() # reverse the list in place, O(n) time complexity
print(xs)
ys = sorted(xs) # return a new sorted list, original list unchanged
print(ys, xs)
zs = sorted(xs, key=lambda x: -x) # sort in reverse order using a key function
zs = sorted(xs, reverse=True) # sort in reverse order using the reverse parameter, better than using a key function for reverse sorting

# === 6. Tuples ===

print("-- tuples --")

t = (1, 2, 3)
t2 = 1, 2, 3 # parentheses are optional for tuples
singleT = (1,) # need a comma for single element tuple
singleT2 = 1, # same as above
emtpyT = () # empty tuple
print(t, t2, singleT, singleT2, emtpyT)
# Immutable - can't change afer creation, but can contain mutable objects
t = (1, 2, [3, 4])
t[2][0] = 99 # can modify the mutable object inside the tuple
print(t)
# tupe unpacking
def min_max(nums):
    return min(nums), max(nums)
lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)
pointSet = {(0, 0), (1, 2), (3, 4)}
print(pointSet)
pointCountDict = {(0, 0): 1, (1, 2): 3, (3, 4): 2}
print(pointCountDict)
print(pointCountDict[(1, 2)])

# === 7. Sets ===

print("-- sets --")

s = {1, 2, 3, 4, 5, 1} # create a set using curly braces, duplicates are automatically removed
s2 = set([3, 4, 5, 6, 7]) # create a set from an iterable
print(s, s2)
emptyS = set() # create an empty set, can't use {} because it creates an empty dictionary

# Set operations
print(3 in s) # membership test
print(len(s)) # number of elements in the set
s.add(6) # add an element to the set
s.add(7) # add an element to the set
s.add(8) # add an element to the set
s.remove(1) # remove an element from the set, raises KeyError if the element is not found
s.discard(1) # remove an element from the set, does nothing if the element is not found
s.update([7, 8, 9]) # add multiple elements to the set
s |= {7, 8, 9} # same as update
s &= {3, 4, 5} # keep only elements that are also in another set
s -= {3, 4} # remove elements that are also in another set
s ^= {4, 5} # keep only elements that are in either set, but not both
print(s)

# === 8. Dictionaries ===

print("-- dictionaries --")

d = {"one": 1, "two": 2, "three": 3} # create a dictionary using curly braces, key-value pairs separated by colons
d2 = dict(one=1, two=2, three=3) # create a dictionary using the dict constructor with keyword arguments
print(d, d2)
emptyD = {} # create an empty dictionary, same as dict(), {} is not an empty set, it's an empty dictionary
print(emptyD)

print(d["two"]) # access a value by key
print(d.get("two")) # same as above, but returns None if the key is not found instead of raising KeyError
print(d.get("four", 4)) # return a default value if the key is not found
d["four"] = 4 # add a new key-value pair to the dictionary
d["two"] = 22 # update the value for an existing key
del d["three"] # remove a key-value pair from the dictionary
d.pop("three", None) # same as above, but does nothing if the key is not found

# dictionary iteration
for k in d:
    print(k, d[k]) # iterate over keys and access values
for k, v in d.items():
    print(k, v) # iterate over key-value pairs
for v in d.values():
    print(v) # iterate over values

# === 9. Comparison + Identity ===

print("-- comparison and identity --")

# == is Vlue equality, calls the __eq__ method of the objects, can be overridden by custom classes
print([1, 2, 3] == [1, 2, 3]) # True, because the contents are the same
# is is reference equality, checks if two variables point to the same object in memory
print([1, 2, 3] is [1, 2, 3]) # False, because they are different objects in memory
a = [1, 2, 3]
b = a
print(a is b) # True, because a and b point to the same object in memory
print(id(a), id(b)) # id() returns the memory address of the object, and b have the same id because they point to the same object

x = None
print(x is None) # True, because x is None
print(x == None) # True, but it's recommended to use is for None comparison

# chain comparison
x = 5
print(0 < x < 10) # True, because x is greater than 0 and less than 10
print(0 < x > 3) # True, because x is greater than 0 and greater than 3
print(0 < x < 3) # False, because x is not less than 3

print("one" in {"one": 1}) # True, because the key "one" is in the dictionary
print(1 in {"one": 1}) # False, because the value 1 is not a key in the dictionary

# == 10. Control Flow ===

print("-- control flow --")

n = 7
if n < 5: # no parentheses around the condition, but the colon is required to start the block
    print("n is less than 5")
elif n < 10: # elif is short for else if, can have multiple elif branches, but only one will be executed
    print("n is between 5 and 10")
else:
    print("n is 10 or greater")

# Ternary operator - conditional expression
label = "small" if n < 5 else "medium" if n < 10 else "large" # small if n < 5, medium if n < 10, otherwise large, evaluated from left to right, can be nested but can be hard to read, use parentheses for clarity if needed
print(label)

for i in [10, 20, 30]: # for loop iterates over the elements of a collection, no need for an index variable, but can use enumerate() if index is needed
    print(i)

# range(start, stop, step) generates a sequence of numbers, start is inclusive, stop is exclusive, step can be negative for reverse
for i in range(5): # from 0 to 4
    print(i)
for i in range(2, 5): # from 2 to 4
    print(i)
for i in range(10, 0, -2): # from 10 to 2, step -2
    print(i)

for index, value in enumerate(["a", "b", "c"]): # enumerate() returns pairs of index and value, useful for iterating with an index
    print(index, value)

for name, age in zip(["Alice", "Bob", "Charlie"], [25, 30, 35]): # zip() combines multiple iterables into tuples, useful for iterating over multiple collections in parallel
    print(name, age)
for name, age in zip(["Alice", "Bob", "Charlie"], [25, 30, 35, 50]): # zip() stops when the shortest iterable is exhausted
    print(name, age)
for i, (name, age) in enumerate(zip(["Alice", "Bob", "Charlie"], [25, 30, 35])): # can combine enumerate and zip for indexed parallel iteration
    print(i, name, age)

for i in range(5):
    if i % 2 == 0:
        continue # skip the rest of the loop body and move to the next iteration
    print(i)
for i in range(5):
    if i == 3:
        break # exit the loop immediately
    print(i)

while n > 0:
    print(n)
    n -= 1

# === 11.Comprehensions ===

print("-- comprehensions --")

# list comprehension
squares = [x ** 2 for x in range(10)] # create a list of squares from 0 to 9
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x ** 2 for x in range(10) if x % 2 == 0] # create a list of squares of even numbers from 0 to 9
print(even_squares) # [0, 4, 16, 36, 64]

# Transforming and filtering with comprehensions
pairs = [(i, x) for i, x in enumerate("abcde")] # create a list of pairs of index and character from the string
print(pairs) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

# Nested comprehensions
grid = [[(i, j) for j in range(3)] for i in range(3)] # create a 3x3 grid of coordinate pairs
print(grid) # [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
coords = [(i, j) for i in range(4) for j in range(3)] # same as above, but with a single comprehension, evaluated from left to right
print(coords) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
# flatten a grid
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = -1
flattened = [y for row in grid for y in row]
print(flattened) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dict comprehension
d = {x: x * x for x in range(5)} # create a dictionary mapping numbers to their squares
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
s = {x ** 3 for x in range(10) if x % 2 == 1} # create a set of cubes of odd numbers from 0 to 9
print(s) # {1, 27, 729, 343, 125}

# Generator expression - creates an iterator that generates values on the fly, can be used with functions like sum() or to create a list with list()
gen = (x ** 2 for x in range(100)) # create a generator of squares from 0 to 99
next(gen) # 0
next(gen) # 1
next(gen) # 4
numberSum = sum(x for x in range(10)) # sum of squares from 0 to 9, using a generator expression inside the sum() function
print(numberSum) # 45

# === 12. Functions ===

print("-- functions --")

# Function definition
def greet(name):
    return f"Hello, {name}!" # return a greeting message using an f-string
print(greet("Bo")) # Hello, Bo!

# Default arguments
def power(base, exponent=2):
    return base ** exponent # return the result of raising base to the power of exponent, default is 2 for squares
print(power(3)) # 9, because exponent defaults to 2
print(power(3, 3)) # 27, because exponent is specified as 3

# Variable-length arguments
def sum_all(*args):
    return sum(args) # return the sum of all arguments, *args collects all positional arguments into a tuple
print(sum_all(1, 2, 3)) # 6

def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}") # print each key-value pair, **kwargs collects all keyword arguments into a dictionary
print_key_values(name="Alice", age=30, city="New York") # name: Alice, age: 30, city: New York

def mixed_args(*args, **kwargs):
    print("Positional arguments:", args) # print the tuple of positional arguments
    print("Keyword arguments:", kwargs) # print the dictionary of keyword arguments
mixed_args(1, 2, 3, name="Alice", age=30)

# type hints - optional annotations for function parameters and return types, not enforced at runtime but can be used by static type checkers
def add(x: int, y: int) -> int:
    return x + y
print(add(3, 4)) # 7

# multiple return values
def min_max(nums):
    return min(nums), max(nums) # return a tuple of the minimum and maximum values in the list
lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi) # 1 5

# Lambda functions - anonymous functions defined with the lambda keyword, can be used for short, throwaway functions
square = lambda x: x * x # create a lambda function that squares its input
print(square(5)) # 25
nums = [(1, "b"), (2, "a"), (3, "c")]
print(sorted(nums, key=lambda x: -x[0])) # sort the list of tuples in reverse order based on the first element of the tuple, using a lambda function as the key

# don't initialize mutable default arguments like lists or dictionaries, because they are shared across all calls to the function, use None and create a new object inside the function instead
def append_to_list(value, lst=None):
    if lst is None:
        lst = [] # create a new list for each call if lst is not provided
    lst.append(value)
    return lst
print(append_to_list(1)) # [1]
print(append_to_list(2)) # [2], not [1, 2]

# === 13. Classes ===

print("-- classes --")

class Point:
    # Constructor method, called when a new instance is created
    def __init__(self, x, y): # constructor name is always __init__, self is the instance being created, x and y are parameters for the constructor
        self.x = x # assign the x parameter to an instance variable
        self.y = y # assign the y parameter to an instance variable
    
    # Instance Method - first parameter is always self, which refers to the instance on which the method is called
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5 # calculate the distance from the point to the origin using the Pythagorean theorem
    
    # __repr__ method - defines the string representation of the object, used by the repr() function and in the interactive interpreter
    def __repr__(self):
        return f"Point({self.x}, {self.y})" # return a string representation of the point

p = Point(3, 4) # create a new instance of the Point class
print(p) # Point(3, 4), calls the __repr__ method to get the string representation of the point
print(p.distance_to_origin()) # 5.0, calls the distance_to_origin method on the point instance

# Leetcode's expected class definition:
class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # implementation goes here
        pass
