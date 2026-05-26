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

# === 14 collections.Counter ===

print("-- collections.Counter --")

from collections import Counter
c = Counter("banana") # create a Counter object from a string, counts the frequency of each character
print(c) # Counter({'a': 3, 'n': 2, 'b': 1})
print(c["a"]) # 3, count of 'a'
print(c["x"]) # 0, count of 'x', returns 0 for missing keys instead of raising KeyError
c["a"] += 1 # increment the count of 'a' by 1
print(c) # Counter({'a': 4, 'n': 2, 'b': 1})
c.update("apple") # update the counts with another string, adds the counts of characters in "apple" to the existing counts
print(c) # Counter({'a': 5, 'p': 2, 'l': 1, 'e': 1, 'n': 2, 'b': 1})
most_common = c.most_common(2) # get the 2 most common elements and their counts, time complexity is O(n log k) where n is the number of unique elements and k is the number of most common elements to return
print(most_common) # [('a', 5), ('n', 2)]

# Counter artithmetic operations
a = Counter("aabbc")
b = Counter("abccd")
print(a + b) # Counter({'a': 3, 'b': 3, 'c': 3, 'd': 1}), addition combines counts, keeps only positive counts
print(a - b) # Counter({'a': 1, 'b': 1}), subtraction subtracts counts, keeps only positive counts
print(a & b) # Counter({'a': 1, 'b': 1}), intersection takes the minimum of counts
print(a | b) # Counter({'a': 3, 'b': 3, 'c': 3, 'd': 1}), union takes the maximum of counts

# Equality - two Counter objects are equal if they have the same counts for all elements, even if they have different keys with zero counts
c1 = Counter("aabb")
c2 = Counter("aabb") + Counter("cc") - Counter("cc") # Counter({'a': 2, 'b': 2}), c1 and c2 have the same counts for 'a' and 'b', and both have zero counts for 'c', so
print(c1 == c2) # True

# Mutation
c.update("abc") # update the counts with another string, adds the counts of characters in "abc" to the existing counts
c.subtract("ab") # subtract the counts with another string, subtracts the counts of characters in "ab" from the existing counts

# === 15. collections.defaultdict ===

print("-- collections.defaultdict --")

# A dict that auto-creates missing keys using a factory function provide. The factory function is called with no arguments to create a default value when a missing key is accessed. This can be useful for counting, grouping, or accumulating values without having to check if the key already exists in the dictionary.
from collections import defaultdict
ddict = defaultdict(int) # create a defaultdict with int as the default factory, missing keys will have a default value of 0
for ch in "banana":
    ddict[ch] += 1 # increment the count for each character, no need to check if the key exists because defaultdict will create it with a default value of 0
print(ddict) # defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2})
print(ddict["x"]) # 0, accessing a missing key returns the default value of 0
ddict["x"] += 1 # increment the count for 'x', now 'x' will have a count of 1
print(ddict) # defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2, 'x': 1})

ddict = defaultdict(list) # create a defaultdict with list as the default factory, missing keys will have a default value of an empty list
words = ["bat", "ball", "cat", "car", "dog"]
for w in words:
    key = "".join(sorted(w)) # sort the characters in the word to create a key for anagrams
    ddict[key].append(w) # append the word to the list of anagrams for that key
print(ddict) # defaultdict(<class 'list'>, {'abt': ['bat', 'tab'], 'abl': ['ball'], 'act': ['cat'], 'acr': ['car'], 'dgo': ['dog']})

graph = defaultdict(set) # create a defaultdict with set as the default factory, missing keys will have a default value of an empty set
edges = [(1, 2), (1, 3), (2, 3), (3, 4)]
for u, v in edges:
    graph[u].add(v) # add v to the set of neighbors for u
    graph[v].add(u) # add u to the set of neighbors for v, assuming an undirected graph
print(graph) # defaultdict(<class 'set'>, {1: {2, 3}, 2: {1, 3}, 3: {1, 2, 4}, 4: {3}})

nested = defaultdict(lambda: {"count": 0, "items": []}) # create a defaultdict with a lambda function as the default factory, missing keys will have a default value of a dictionary with count and items
nested["a"]["count"] += 1 # increment the count for key 'a', now nested['a'] will have {'count': 1, 'items': []}
nested["a"]["items"].append(1) # append 1 to the items list for key 'a', now nested['a'] will have {'count': 1, 'items': [1]}
print(nested) # defaultdict(<function <lambda> at 0x7ff8c0d0>, {'a': {'count': 1, 'items': [1]}}})

# when trying to access a missing key in a defaultdict, the default factory function will be called to create a default value, and that value will be added to the dictionary with the missing key. This means that if you access a missing key multiple times, it will create multiple entries in the dictionary with the same default value, which can lead to unexpected behavior if the default value is mutable (like a list or a dictionary). To avoid this, it's important to use an immutable default value or to ensure that the default factory function creates a new object each time it's called.
if "missing" in ddict: # check if the key "missing" is in the dictionary, this will return False because "missing" has not been accessed yet, so it has not been added to the dictionary
    print("missing key exists in the dictionary")


# === 16. collections.deque ===

print("-- collections.deque --")

# double-ended queue, append, appendleft, pop, popleft operations are O(1) time complexity, while list append and pop from the end are O(1) but insert and pop from the beginning are O(n) time complexity, so deque is more efficient for queue and stack operations
from collections import deque
dq = deque([1, 2, 3]) # create a deque with an initial list of elements
print(dq) # deque([1, 2, 3])
dq.append(4) # add an element to the right end of the deque
dq.appendleft(-1) # add an element to the left end of the deque
print(dq) # deque([-1, 1, 2, 3, 4])
dq.pop() # remove and return the rightmost element, returns 4
dq.popleft() # remove and return the leftmost element, returns -1
print(dq) # deque([1, 2, 3])
dq.extend([4, 5]) # add multiple elements to the right end of the deque
dq.extendleft([-2, -3]) # add multiple elements to the left end of the deque, the order of the added elements will be reversed because they are added to the left
print(dq) # deque([-3, -2, 1, 2, 3, 4, 5])
dq.rotate(2) # rotate the deque to the right by 2 steps, the last 2 elements will be moved to the front
print(dq) # deque([4, 5, -3, -2, 1, 2, 3])
dq.rotate(-3) # rotate the deque to the left by 3 steps, the first 3 elements will be moved to the end
print(dq) # deque([-2, 1, 2, 3, 4, 5, -3])

windowdp = deque(maxlen=3) # create a deque with a maximum length of 3, when the deque exceeds this length, the oldest elements will be automatically removed from the left
windowdp.extend([1, 2, 3]) # add elements to the deque
windowdp.append(4) # add an element to the right end of the deque, now the deque will have [2, 3, 4] because the oldest element 1 is removed to maintain the maxlen of 3
print(windowdp) # deque([2, 3, 4], maxlen=3)
windowdp.appendleft(0) # add an element to the left end of the deque, now the deque will have [0, 2, 3] because the oldest element 4 is removed to maintain the maxlen of 3
print(windowdp) # deque([0, 2, 3], maxlen=3

# always dequeue for queues, and use append for stacks, but deque can be used for both queues and stacks efficiently

# === 17. heapq - priority queue ===

print("-- heapq --")
import heapq

h = [] # create an empty list to be used as a heap
heapq.heappush(h, 5) # add an element to the heap, maintains the heap property
heapq.heappush(h, 2) # add another element to the heap
heapq.heappush(h, 8) # add another element to the heap
print(h) # [2, 5, 8], the smallest element is at the root of the heap
smallest = heapq.heappop(h) # remove and return the smallest element from the heap, maintains the heap property
print(smallest) # 2
print(h) # [5, 8], the heap is updated after popping the smallest element
heapq.heappush(h, 1) # add another element to the heap
print(h) # [1, 8, 5], the smallest element is now 1
smallest = heapq.heappop(h) # remove and return the smallest element from the heap
print(smallest) # 1
print(h) # [5, 8], the heap is updated after popping the smallest element

nums = [5, 2, 8, 1, 3]
heapq.heapify(nums) # transform the list into a heap in-place, O(n)
print(nums) # [1, 2, 8, 5, 3], the smallest element is at the root of the heap

heapq.heappushpop(nums, 4) # push a new element and pop the smallest element in one operation, more efficient than doing heappush followed by heappop
print(nums) # [2, 3, 8, 5, 4], the smallest element 1 is removed and 4 is added to the heap
heapq.heapreplace(nums, 6) # pop the smallest element and push a new element in one operation, more efficient than doing heappop followed by heappush
print(nums) # [3, 4, 8, 5, 6], the smallest element 2 is removed and 6 is added to the heap

print(heapq.nsmallest(2, nums)) # get the 2 smallest elements from the heap, O(k log n) where k is the number of smallest elements to return
print(nums) # [3, 4, 8, 5, 6], the original heap is unchanged
print(heapq.nlargest(2, nums)) # get the 2 largest elements from the heap, O(k log n) where k is the number of largest elements to return
print(nums) # [3, 4, 8, 5, 6], the original heap is unchanged

max_h = [] # create an empty list to be used as a max heap, we can use a min heap to implement a max heap by negating the values
heapq.heappush(max_h, -5) # add an element to the max heap
heapq.heappush(max_h, -2) # add another element to the max heap
heapq.heappush(max_h, -8) # add another element to the max heap
print(max_h) # [-8, -2, -5], the largest element is at the root of the max heap (negated)
largest = -heapq.heappop(max_h) # remove and return the largest element from the max heap, negate it back to get the original value
print(largest) # 8

task = []
heapq.heappush(task, (3, "low priority task")) # add a task with a priority of 3
heapq.heappush(task, (1, "high priority task")) # add a task
heapq.heappush(task, (2, "medium priority task")) # add a task
print(task) # [(1, 'high priority task'), (3, 'low priority task'), (2, 'medium priority task')], the task with the highest priority (lowest number) is at the root of the heap

# === 18. bisect - binary search ===

print("-- bisect --")
import bisect

sorted_list = [1, 3, 5, 7, 9] # create a sorted list, bisect functions assume the list is already sorted
index = bisect.bisect_left(sorted_list, 5) # find the index where 5 should be inserted to maintain sorted order, if 5 is already in the list, it returns the index of the leftmost 5
print(index) # 2
index = bisect.bisect_right(sorted_list, 5) # find the index where 5 should be inserted to maintain sorted order, if 5 is already in the list, it returns the index of the rightmost 5
index = bisect.bisect(sorted_list, 5) # same as bisect_right
print(index) # 3
bisect.insort(sorted_list, 6) # insert 6 into the sorted list while maintaining sorted order
print(sorted_list) # [1, 3, 5, 6, 7, 9], 6 is inserted at the correct position to maintain sorted order

def contains(nums, target):
    index = bisect.bisect_left(nums, target) # find the index where target should be inserted
    return index < len(nums) and nums[index] == target # check if the target is actually present at that index

def count_occurrences(nums, target):
    left_index = bisect.bisect_left(nums, target) # find the leftmost index of target
    right_index = bisect.bisect_right(nums, target) # find the rightmost index of target
    return right_index - left_index # return the count of occurrences

# === 19. quick hits ===

print("-- quick hits --")
import itertools, math, string

ids = itertools.count(1) # create an infinite iterator that generates consecutive integers starting from 1
print(next(ids)) # 1
print(next(ids)) # 2

print(list(itertools.chain([1, 2], [3, 4]))) # [1, 2, 3, 4], chain combines multiple iterables into a single iterable
print(list(itertools.combinations("abc", 2))) # [('a', 'b'), ('a', 'c'), ('b', 'c')], combinations generates all possible combinations of a given length from the input iterable
print(list(itertools.permutations("abc", 2))) # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')], permutations generates all possible permutations of a given length from the input iterable
print(list(itertools.product("ab", "12"))) # [('a', '1'), ('a', '2'), ('b', '1'), ('b', '2')], product generates the Cartesian product of the input iterables
for r, c in itertools.product(range(3), range(4)):
    print(r, c) # prints all pairs of row and column indices for a 3x4 grid

print(math.inf) # positive infinity
print(-math.inf) # negative infinity
print(math.gcd(48, 18)) # greatest common divisor of 48 and 18, returns 6
print(math.lcm(12, 18)) # least common multiple of 12 and 18, returns 36
print(math.isqrt(16)) # integer square root of 16, returns 4
print(math.log2(8)) # logarithm base 2 of 8, returns 3.0
print(math.ceil(2.3)) # ceiling of 2.3, returns 3
print(math.floor(2.7)) # floor of 2.7, returns 2
print(divmod(7, 3)) # returns the quotient and remainder of 7 divided by 3 as a tuple, returns (2, 1)

print(string.ascii_lowercase) # 'abcdefghijklmnopqrstuvwxyz', a string containing all lowercase letters
print(string.ascii_uppercase) # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', a string containing all uppercase letters
print(string.digits) # '0123456789', a string containing all digits
