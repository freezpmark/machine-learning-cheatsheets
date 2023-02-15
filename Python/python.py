# Variable init, Output function (Shellable)
word = "school"	# no need to declare data type (int/float/str/bool)
                  	# variable must start with letter/underscore, after can use num
a, b = (1, 2)		# we can also assign multiple variables (a, b = 1, 2 works too)
print("Go to \"" + word + "\"!", f'...{a}')	# Go to "school"! ...1

# 1. Data types
# immutable(hashable) -> int/float/str/bool/classes/tuple/frozenset
# mutable(unhashable) -> list/dict/set

# integers/floats
a = 1
a += 2			# can use + - * / ** // % arithmetic/assignment operators
print(a/2)          # 1.5 changes to float, for int trimmed version (1) use //
print(8.9e-4)   	# 0.00089 for more precision, use decimal package

# strings (useful functions: join, split, find, strip)
name = "Paul"		# to save multiple lines into string use """ (works as comment)
name += " Jef"
print("="*2 + f"Hello {name}")   # ==Hello Paul Jef

# bool
locked = False			# or True 

# COLLECTIONS (can be nested and can contain various types of variables)
# lists
b = list()				# or y = [] for creating empty list
b = [1, 2, 3, "dyna", 'mak', 3]	# [1, 2, 3, 'dyna", 'mak', 3]
b += "BUR"				# [1, 2, 3, 'dyna', 'mak', 3, 'B', 'U', 'R']

# dictionary - is similar to a list, but you access values by looking up a key instead of an index. (keys must be hashable). There is also defaultdict in collections package which will never raise KeyError, instead it will return default value based on the type that was specified (defaultdict(int))
d = {'one' : 1, 'two' : 2, 'three' : 3}
d['four'] = 4
print(d['one'])	# 1

# sets - are unordered collections that contain only unique and hashable elements, they're displayed in {} brackets, use set() to create empty set because {} is for dict. There are also frozensets that are immutable -> cannot be changed
print(set(["FILE", "FiLe"]) - {"FILE", "file"}) # {'FiLe'}

# tuples
c = 'dan', "svk", "cze"		# or ('dan', "svk", "cze") 

# namedtuples (can convert to dict with _asdict())
import collections
Sales = collections.namedtuple("Sale", "productid price")
record = Sales(11, 4.5)
print(record, record[1], record.price)	 # Sale(productid=11, price=4.5) 44.1 44.1 

# COLLECTION COPYING
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# no copy - references will be the same
re_list = old_list

# shallow copy - copies first level elements (also list(old_list) or old_list [:])
copy_list = copy.copy(old_list)

# deep copy - recursively copies all elements inside a variable
deepcopy_list = copy.deepcopy(old_list)

re_list.append([11, 12])
copy_list.append([4, 4, 4])
deepcopy_list[1][0] = 'BB'

print(old_list)         	# [[1, 1, 1], [2, 2, 2], [3, 3, 3], [11, 12]]
print(re_list)		# [[1, 1, 1], [2, 2, 2], [3, 3, 3], [11, 12]]
print(copy_list)        	# [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
print(deepcopy_list)	# [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]

# COLLECTION SLICING SYNTAX
# The default starting index is 0
# The default ending index is the end of the list
# The default stride is 1

l = [i ** 2 for i in range(1, 10)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(l[2:8:2])                     # [9, 25, 49]

to_five = ['A', 'B', 'C', 'D', 'E']
print(to_five[3:])       # ['D', 'E']
print(to_five[:2])       # ['A', 'B']
print(to_five[::2])      # ['A', 'C', 'E']
to_five[0:2] = ['Z', 'X']
print(to_five)           # ['Z', 'X', 'C', 'D', 'E']

# 2. Basic built-in functions
print(type(5))      		# <class 'int'> writes type of variable
print(int("  3333  "))		# 3333 int type removes string spaces
print(max([2, 4, 6]))		# 6
print(len([2, 4, 6, "kda"]))	# 4 works for all iterable objects
print(sum([2, 4, 8, 16]))		# 30
print(sorted([4, 2, 4, 3, 1]))	# 1, 2, 3, 4, 4 works for str too
print(any([0, 1, 0])) 		# True return True if there's one True, else False
print(all([1, 1, 1])) 		# True return True if all are true, else False
# print(help(dir))			# writes documentation of dir function, q to quit
vst = input("Enter something: ")	# Enter something: saves input into vst
del vst  	     			# deletes and relieves var from memory


# 3. Operators
# comparison operator   	# can also compare strings (alphabetically)
print(0 < 5 < 10 < 20)   	# True can also use < <= == !=

# membership operator - in 	# works for collections (linear complexity)
p = (4, "zaba", 9, -33, 9, 2)
p2 = "colorful calculator"
print(2 in p)       	# True
print("color" in p2)  	# True

# identity operator - is
a = ["string", 4, None]
b = ["string", 4, None]
print(a is b)   # False
b = a
print(a is b)   # True

# logical operator
# NOT, AND and OR uses short circuiting technique and returns operand that determines the result. Order of evaluation is: not, >, and, >, or. But we can change it with the brackets
# special object None, empty collection or 0 number returns logical expression FALSE, everything else is TRUE
five = 5
two = 2
print(five and two)		# 2

# Program Control Flow
# 4. Conditions
lines = 5000
if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")   	# medium
else:
    print("large")

count = 100 + 10 if True else 0

# 5. Cycles
countries = ["Slovakia", "Sweden", "Czechia"]
i = 0
while i < 3:
     print(countries[i])	# Slovakia\nSweden\nCzechia
     i += 1
else:			# executes anytime the loop condition is evaluated to False.
     print("End")	# Slovakia\nSweden\nCzechia\nEnd

for country in countries:
     print(country)		# Slovakia\nSweden\nCzechia

for index, country in enumerate(countries, 1):  # (useful functions: range)
     print(country)		# Slovakia\n1. country was printed!\nSweden\n
     if index == 1:
          print("1. country was printed!")
     if index < 3:
          continue
     break

for i, j in ([1, 3], [2, 4]):
     print(i, j)		 # 1 3\n2 4

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):	# stops at the end of one collection
     print(a if a >= b else b)	# 3\n 9\n 17\n 15\n 30\n

# 6. Exceptions
s = input("Write whole number: ")
try:
    i = int(s)	# any error in try block will be catched in except with msg
    print(i, "is ok")
except ValueError as err:	# as is optional, and also is the ValueError 
    print(err)
except TypeError as err2:
    print(err2)
    exit()  # return is not enough if we want to end program in nested function
else:
    print("There was no exception")
finally:
    print("This message is written every time")

# there is hierarchy of exceptions
# we can create our own exceptions by making a class with inheritance in arg

class myException(Exception): pass	# Exception is a base exception, by pass we are telling the program to do nothing. It can be used in functions or exceptions

# assert logical_expr, error_msg		# raises an exception if condition is false
# if cond == False:
# 	raise AssertionError("text") 	# raises an exception
# raise alone reraises the parsing exception inside except block
# example below shows how we can make exception grouped together with isinstance

class InvalidEntityError(Exception): pass
class InvalidNumericEntityError(InvalidEntityError): pass
class InvalidAlphaEntityError(InvalidEntityError): pass
class InvalidTagContentError(Exception): pass


'''
except (InvalidEntityError,                 # BASE E
        InvalidTagContentError) as err:     # BASE T
        if isinstance(err, InvalidNumericEntityError):
            error = "wrong number entity"
        elif isinstance(err, InvalidAlphaEntityError):
            error = "wrong alphabetical entity"
        elif isinstance(err, InvalidTagContentError):
            error = "wrong character"
        print(f"Error {error} in {filename} on line {lino} in column {column}")
        if skip_on_first_error:
            raise
'''

# isinstance(object, Point) checks whether object is the same class as Point or one of its base classes
# when we are nested deeply, raising exception to get outside is the best way, instead of breaking from each outer loop

# 7. Functions
def ask_ok(prompt, retries=4, complaint='Yes or no!'):
	return prompt + str(retries) + complaint

print(ask_ok('Want to quit?', complaint='What?'))	# Want to quit?4What?

# args with initialized value inside function (keyworded arg) is called optional arg, otherwise it is mandatory arg (positional arg)
# optional args have a default value
# after stating keyword arg, we must continue with keyword args
# we can pass keyword args to positional args too
# passed mutable objects are being changed outside function, immutable ones not
# for readability use all positional args or all keyword args (?!)
# https://stackoverflow.com/questions/7041752/any-reason-not-to-always-use-keyword-args

# if we don't pass lst arg, appended x will persist in lst for next calls
def append_if_even(x, lst=[]):
    if x % 2 == 0:
        lst.append(x)
    return lst	# irrelevant if we pass lst arg

# * (extraction) captures all positional args given to the product
# if we put another function’s arg, we have to pass keyword arg.
def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(product(2, 3, 4))

# pass infinite number of non-keyword and keyword args
def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print("positional arg {0} = {1}".format(i, arg))
    for key in kwargs:
        print("keyword arg {0} = {1}".format(key, kwargs[key]))

pole1 = [1, 2, 3]
pole2 = [4, 5, 6]
dict1 = {"paper": "A4", "color": "True"}
print_args(pole1, *pole2, dict1, *dict1, **dict1, surname="Markus")

# positional arg 0 = [1, 2, 3] 	pole1
# positional arg 1 = 4		*pole2
# positional arg 2 = 5		*pole2
# positional arg 3 = 6		*pole2
# positional arg 4 = {'paper': 'A4', 'color': 'True'}		dict1
# positional arg 5 = paper				*dict1
# positional arg 6 = color				*dict1
# keyword arg paper = A4				**dict1
# keyword arg color = True				**dict1
# keyword arg surname = Markus			surname="Markus"

# if we want to force passing keyword args, we have to put * before them
# this function requires all of its args to be specified using their name

from random import choice, shuffle


UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = UPPERCASE.lower()
DIGITS = "0123456789"
ALL = UPPERCASE + LOWERCASE + DIGITS


def random_password(*, upper=1, lower=1, digits=1, length=8):
    chars = [
        *(choice(UPPERCASE) for _ in range(upper)),
        *(choice(LOWERCASE) for _ in range(lower)),
        *(choice(DIGITS) for _ in range(digits)),
        *(choice(ALL) for _ in range(length-upper-lower-digits)),
    ]
    shuffle(chars)
    return "".join(chars)


print(random_password(upper=1, lower=1, digits=1, length=8))

# tuple unpacking
fir, sec, *remains = [1, 2, 3, 4, 5]
print(remains)		# [3, 4, 5]

# unpacking into function call
fruits = ['apple', 'pear', 'orange']
print(*fruits)		# apple pear orange

# unpacking keyword args
date_info = {'year': "2020", 'month': "01", 'day': "01"}
filename = "{year}-{month}-{day}.txt".format(**date_info) # '2020-01-01.txt'

# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

# Files, Directories, Imports
# 8. Files I/O
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")		# “r” is default
for i in my_list:
    my_file.write(str(i) + "\n")
my_file.close()

my_file = open("output.txt")		# iteration element of file is one line 
print(my_file.read())
my_file.close()

# https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function

# 9. Imports
import math, os
import os.path as pa			# OR from os import path as pa
from os.path import *			# imports all methods except private ones

# print(os.path.basename(filename))	# safe approach
# print(pa.basename(filename))		# no risk of overriding with pa name
# print(basename(filename))    		# risk of overriding name of methods

# CREATING OUR OWN PACKAGE
# Graphics/
#     __init__.py
#     Bmp.py
#     Jpeg.py
#     Vector/
#          __init__.py
#          Eps.py
# 	         import Graphics.Png as Png	# explicit path
#          Svg.py
# 	         import ..Graphics import Png	# relative path

# we can create our own global packages in C:\Users\<user>\AppData\Roaming\Python\Python38\site-packages
# __init__.py https://stackoverflow.com/questions/448271/what-is-init-py-for#:~:text=The%20__init__.py%20file%20makes%20Python%20treat%20directories,the%20submodules%20to%20be%20exported.
# https://realpython.com/python-modules-packages/ If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.

# relative imports https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

# running the module as a program - will be called only when we run this by itself
if __name__ == "__main__":
    pass

# there are also doctests, which are tests written in documentation, rarely used https://docs.python.org/3/library/doctest.html

# 10. Object oriented programming (OOP) *
# In 1. example:
# We use the word object in parentheses because we want our classes to inherit the object class. This means that our class has all the properties of an object, which is the simplest, most basic class. We can define such class without specifying the object arg., It is set by default.

# There are 4 kinds of functions:
# normal - basic function of a module that can be imported
# method - relates to the instance of a class. We can access them via self that are being passed as the first parameter.
# special - also known as magic methods that are predefined and are being called behind the scenes. They are surrounded by underscores (__<methodName>__)
# classmethod - relates to the class only, not its instances. We can access them via cls that are being passed as the first parameter.
# staticmethod - acts as a normal method, but it exists inside a class, use it when you don't access the instance or class within the function

# There are 4 kinds of variables:
# global - we can use global variable in function, but it will act as a local variable unless we declare it with global keyword (global <global_variable>)
# nonlocal - causes the variable to refer to the previously bound variable in the closest enclosing scope. In other words, it will prevent the variable from trying to bind locally first, and force it to go a level 'higher up'. Useful in nested functions. (nonlocal <variable>)

def myfunc1():
    x = "John"
    def myfunc2():
        nonlocal x
        x = "hello"


    myfunc2()
    return x


print(myfunc1())  # hello


# instance - entity or object that is tied to a class
# class - is tied with all instances, if we change a class variable from within an instance, this instances tie with class is broken and therefore acts as instance variable (not recommended to set this variable within an instance)











# In 2. example:
# If we want to call a method that is being overriden, use super().<method_name>

# Polymorphism
# Duck Typing - type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute. (we are not concerned about which object class it is, we are concerned about the method name it calls)
# Operator Overloading - __add__ method
# Method Overloading - same method name, but args or their type are different (it is not supported in Python, but can code it via “trick” with opt. args)
# Method Overriding - you have two methods with the same and args, the one that was inherited from the super class got overridden
# https://www.programiz.com/python-programming/polymorphism

# full codes + OOP Shaffer https://github.com/CoreyMSchafer/code_snippets/blob/master/Object-Oriented/3-Class-Static-Methods/oop.py https://github.com/CoreyMSchafer/code_snippets/blob/master/Object-Oriented/6-property-decorator/oop.py https://github.com/CoreyMSchafer/code_snippets/blob/master/Object-Oriented/4-Inheritance/oop-finish.py

class Employee(object):
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1


    @property  # getter
    def fullname(self):
        return f'{self.first} {self.last}'


    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('John', 'Smith', 50000)
emp_1.fullname = "Corey Schafer"


Employee.set_raise_amt(1.05)
print(Employee.raise_amt)   # 1.05
print(emp_1.raise_amt)      # 1.05


new_emp_1 = Employee.from_string('John-Doe-70000')
print(new_emp_1.pay)    # 7000


import datetime
my_date = datetime.date(2020, 8, 20)
print(Employee.is_workday(my_date))  # True


# Polymorphism - Duck typing
class A:
    def __init__(self):
        print("init in A")


    def feat1(self):
        print("Feat 1A")


class B:


    def feat1(self):
        print("Feat 1B")


    def feat2(self):
        print("Feat 4B")


# Multiple inheritance (uses Method Resolution Order - defs order of inheritance)
class C(A, B):
    def __init__(self):
        super().__init__()
        print("init in C")
    def feat3(self):
        print("Feat 5C")


# Nested Classes
class Exe:
    def __init__(self):
        self.args = self.Args("-v")


    def feat(self, fea):
        fea.feat1()


    class Args:
        def __init__(self, args):
            self.args2 = args


cins = C()          # init in A \n init in C
cins.feat1()        # Feat 1B


feat_a = A()        # init in A
feat_b = B()
exe = Exe()
exe.feat(feat_a)    # Feat 1A
exe.feat(feat_b)    # Feat 1B
exe.args.args2      # -v


exe2 = Exe.Args("-r")
exe2.args2          # -r


# SINGLE TRAILING UNDERSCORE
# This convention is used to avoid conflict with Python keywords or built-ins.


# SINGLE LEADING UNDERSCORE
# _single_leading_underscore: weak "internal use" indicator. It's being used as a convention for declaring privacy. _ is used to hide any method when the module is imported using wildcard(*). E.g. from M import * does not import objects whose name starts with an underscore.


# DOUBLE LEADING UNDERSCORE
# Double underscore will mangle the attribute names of a class with class name to avoid conflicts of attribute names between (inherited) classes. The mangling rule of Python is adding the “_ClassName” to front of attribute names that are declared with double underscore. That is, if you write a method named “__method” in a class, the name will be mangled in “_ClassName__method” form. Because it is mangled, we can't access it with “ClassName.__method”. 
# It should not be used to create a private method. It should be used to avoid your method being overridden by a subclass or accessed accidentally. When you create a method starting with __ it means that you don't want anyone to be able to override it, and you only intend to access it from inside its own class.


# Double underscores attributes (special methods)
class Foo:
    def __init__(self):
        self.__spam = 'spam'


    def get_spam(self):
        return self.__spam


class ExtendsFoo(Foo):
    def __init__(self):
        super().__init__()  # without this, we can't call: get_spam()/_Foo__spam
        self.__spam = 'extended spam'


    def get_extended_spam(self):
        return self.__spam


extended_foo = ExtendsFoo()
# print(extended_foo.__spam)                # object has no attribute '__spam'
print(extended_foo.get_spam())              # spam
print(extended_foo.get_extended_spam())     # extended spam
print(extended_foo._Foo__spam)              # spam
print(extended_foo._ExtendsFoo__spam)       # extended spam




# Advanced programming techniques
# 11. Further Procedural programming
# 1. Branching Using Dictionaries
def add_dvd(db): return db
def edit_dvd(db): return db
def list_dvds(db): return db
action = "a"
db = 5


if action == "a":
    add_dvd(db)
elif action == "e":
    edit_dvd(db)
elif action == "l":
    list_dvds(db)
elif action == "q":
    quit(db)
 
functions = dict(
    a=add_dvd, e=edit_dvd,
    l=list_dvds, q=quit
)
print(functions[action](db))



# 2. Generator Expressions and Functions
def items_in_key_order(d):
    for key in sorted(d):
        yield key, d[key]
# is same as:
def items_in_key_order(d):
    return ((key, d[key])
        for key in sorted(d))


def quarters(next_quarter=0.0):
    while True:
        yield next_quarter
        next_quarter += 0.25


# This function will return 0.0, 0.25, 0.5, and so on, forever. 
# Here is how we could use the generator:
result = []
for x in quarters():
    result.append(x)
    if x >= 1.0:
        break
# The break statement is essential—without it the for … in loop will never finish.
# At the end the result list is [0.0, 0.25, 0.5, 0.75, 1.0].


# we can reset generator's current value like this:
def quarters(next_quarter=0.0):
    while True:
        received = (yield next_quarter)
        if received is None:
            next_quarter += 0.25
        else:
            next_quarter = received


# The yield expression returns each value to the caller in turn. 
# In addition, if the caller calls the generator’s send() method, 
# the value sent is received in the generator function as the result
# of the yield expression. Here is how we can use the new generator function:
import sys


result = []
generator = quarters()
while len(result) < 5:
    x = next(generator)
    if abs(x - 0.5) < sys.float_info.epsilon:
        x = generator.send(1.0)
    result.append(x)


# This time the result list is [0.0, 0.25, 1.0, 1.25, 1.5]
# magic-numbers.py

# 3. Dynamic Code Execution (Dynamical importing, Local and Recursive fs.)
# one line dynamic code
x = eval("(2 ** 31) - 1")   # x == 2147483647


# multiple lines of dynamic code
import math
exec('''
def area_of_sphere(r):
    return 4 * math.pi * r ** 2


print(area_of_sphere(3))
''')


# StandardMagicNumbers.py
# WindowsMagicNumbers.py
# IndentedList.py

# 4. Function and Method Decorators
import functools


# with no parameter
def positive_result(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() result isn't >= 0"
        return result
    return wrapper
''' # this is the same as above, @functools.wraps decorator ensures that the wrapper() function has the name and docstring of the original function.


def positive_result(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() result isn't >= 0"
        return result
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper
'''


@positive_result
def discriminant(a, b, c):  # throws an error if the result is negative
    return (b ** 2) - (4 * a * c)


# with more parameters
def bounded(minimum, maximum):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if result < minimum:
                return minimum
            elif result > maximum:
                return maximum
            return result
        return wrapper
    return decorator


@bounded(0, 100)
def percent(amount, total):  # bound percentages between <0;100>
    return (amount / total) * 100



# 5. Function Annotations
# Functions and methods can be defined with annotations—expressions that can be used in a function’s signature. Here’s the general syntax: 


# def functionName(par1: exp1, ..., parN: expN) -> rexp: 
#    pass


# Every colon expression part (: expX) is an optional annotation, and so is the arrow return expression part (-> rexp). The last (or only) positional parameter (if present) can be of the form *args, with or without an annotation; similarly, the last (or only) keyword parameter (if present) can be of the form **kwargs, again with or without an annotation. 
# If annotations are present they are added to the function’s __annotations__ dictionary; if they are not present this dictionary is empty. The dictionary’s keys are the parameter names, and the values are the corresponding expressions. The syntax allows us to annotate all, some, or none of the parameters and to annotate the return value or not. Annotations have no special significance to Python. The only thing that Python does in the face of annotations is to put them in the __annotations__ dictionary; any other action is up to us. Example:


from typing import Dict, FrozenSet, Tuple, Union  
# Union - more types accepted
# Map - is a class type we’ve created


"""
def _held_karp(
    map_: Map, visit_points_amount: int
) -> Tuple[List[Tuple[int, int]], int]:


    coor_and_comb = Tuple[Tuple[int, int], FrozenSet[int]]
    cost_and_parent_coor = Tuple[int, Tuple[int, int]]
    nodes = {}  # type: Dict[coor_and_comb, cost_and_parent_coor]
   # (do some stuff)
    return True
"""




# 12. Further Object-Oriented Programming 
# 1. Controlling Attribute Access
# __slots__         reduces the size of objects (can't create new attrs to class)
# __dict__          dict that stores an object’s (writable) attributes
# __delattr__(self, n)   deletes n attribute in x object               # del x.n
# __dir__(self)          returns list of attribute names in object x   # dir(x)
# __getattr__(self, n)   returns attribute value n of object x with    # v = x.n
# __setattr__(self, n, value)  sets attr n with value v in object x    # x.n = v

# 2. Functors * (+ closures)
import string


# Functor
class Strip:
    def __init__(self, characters):
        self.characters = characters


    def __call__(self, string):
        return string.strip(self.characters)


string_punctuation = Strip(",;:.!?")
string_punctuation("Hello world!")  # Hello world


# We could achieve the same thing using a plain function or lambda, but if we need to store a bit more state or perform more complex processing, a functor is often the right solution. A functor’s ability to capture state by using a class is very versatile and powerful, but sometimes it is more than we really need. Another way to capture state is to use a closure. A closure is a function or method that captures some external state. For example:


# Closure
def make_strip_function(characters):
    def strip_function(string):
        return string.strip(characters)
    return strip_function


strip_punctuation = make_strip_function(",;:.!?")
strip_punctuation("Hello world!")   # Hello world


# The classic use case for functors is to provide key functions for sort routines.
# Here is a generic SortKey functor class (from file SortKey.py):


# When a SortKey object is created it keeps a tuple of the attribute names it was initialized with. When the object is called it creates a list of the attribute values for the instance it is passed—in the order they were specified when the SortKey was initialized. For example, imagine we have a Person class:


# Suppose we have a list of Person objects in the people list. We can sort the list by surnames like this: people.sort(key=SortKey("surname")). If there are a lot of people there are bound to be some surname clashes, so we can sort by surname, and then by forename within surname, like this: people.sort(key=SortKey("surname", "forename")). And if we had people with the same surname and forename we could add the email attribute too.


# Another way of achieving the same thing, but without needing to create a functor at all, is to use the operator module’s operator.attrgetter() function.


class Person:
    def __init__(self, forename, surname, email):
        self.forename = forename
        self.surname = surname
        self.email = email
 
class SortKey:
    def __init__(self, *attribute_names):
        self.attribute_names = attribute_names
 
    def __call__(self, instance):
        values = []
        for attribute_name in self.attribute_names:
            values.append(getattr(instance, attribute_name))
        return values


person1 = Person("Peter", "Markus", "gmail")
person2 = Person("Filip", "Zapletaj", "azet")
person3 = Person("Boris", "Duchon", "gmail")


people = [person1, person2, person3]
people.sort(key=SortKey("surname", "forename"))
print(people)




# SortKey.py

# 3. Context Managers *
# __enter__() and __exit__() allows you to implement objects which can be used easily with the with statement. 
# Context managers allow us to simplify code by ensuring that certain operations are performed before and after a particular block of code is executed. The behavior is achieved because context managers define two special methods, __enter__() and __exit__(), that Python treats specially in the scope of a with statement. When a context manager is created in a with statement its __enter__() method is automatically called, and when the context manager goes out of scope after its with statement its __exit__() method is automatically called.


# The expression must be or must produce a context manager object; if the optional as variable part is specified, the variable is set to refer to the object returned by the context manager’s __enter__() method (and this is often the context manager itself). Because a context manager is guaranteed to execute its “exit” code (even in the face of exceptions), context managers can be used to eliminate the need for finally blocks in many situations.


# Long version:
fh = None
try:
    fh = open(filename)
    for line in fh:
        process(line)
except EnvironmentError as err:
    print(err)
finally:
    if fh is not None:
        fh.close()


# Short version:
try:
    with open(filename) as fh:
        for line in fh:
            process(line)
except EnvironmentError as err:
    print(err)


# can handle multiple context managers in a single with statement.
""" # default behavior with files when using open()
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path) as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
"""


# If we want to create a custom context manager we must create a class that provides two methods: __enter__() and __exit__(). Whenever a with statement is used on an instance of such a class, the __enter__() method is called and the return value is used for the as variable (or thrown away if there isn’t one). When control leaves the scope of the with statement the __exit__() method is called (with details of an exception if one has occurred passed as arguments). Suppose we want to perform several operations on a list in an atomic manner—that is, we either want all the operations to be done or none of them so that the resultant list is always in a known state. For example, if we have a list of integers and want to append an integer, delete an integer, and change a couple of integers, all as a single operation, we could write code like this: If no exception occurs, all the operations are applied to the original list (items), but if an exception occurs, no changes are made at all. Here is the code for the AtomicList context manager:


import copy
 
class AtomicList:
    def __init__(self, alist, deep_copy=False):
        self.original = alist
        self.copy_f = copy.deepcopy if deep_copy else copy.copy
 
    def __enter__(self):
        self.modified = self.copy_f(self.original)
        return self.modified
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:    # exception_type (if exception has not occured)
            self.original[:] = self.modified
 
items = [2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 4


try:
    with AtomicList(items) as atomic:
        atomic.append(58289)
        del atomic[3]
        atomic[8] = 81738
        atomic[index] = 38172
except (AttributeError, IndexError, ValueError) as err:
    print("No changes applied:", err)


print(items)	# [2, 3, 4, 6, 38172, 8, 9, 10, 81738]


# The return value of __exit__() is used to indicate whether any exception that occurred should be propagated. A True value means that we have handled any exception and so no propagation should occur. Normally we always return False or something that evaluates to False in a Boolean context to allow any exception that occurred to propagate. By not giving an explicit return value, our __exit__() returns None which evaluates to False and correctly causes any exception to propagate.



# 4. Descriptors *
# Descriptors are classes which provide access control for the attributes of other classes. Any class that implements one or more of the descriptor special methods, __get__(), __set__(), and __delete__(), is called (and can be used as) a descriptor. The built-in property() and classmethod() functions are implemented using descriptors. The key to understanding descriptors is that although we create an instance of a descriptor in a class as a class attribute, Python accesses the descriptor through the class’s instances.
# https://www.geeksforgeeks.org/descriptor-in-python/

# XmlShadow.py (+cache)
# ExternalStorage.py
# Property.py

# 5. Class Decorators *
# Class decorators take a class object (the result of the class statement), and should return a class—normally a modified version of the class they decorate.

# SortedListDelegate.py (taking methods from default list by delegation)

# 6. Abstract Base Classes *
# An abstract base class (ABC) is a class that cannot be used to create objects. Instead, the purpose of such classes is to define interfaces, that is, to in effect list the methods and properties that classes that inherit the abstract base class must provide. This is useful because we can use an abstract base class as a kind of promise—a promise that any derived class will provide the methods and properties that the abstract base class specifies. # https://www.python.org/dev/peps/pep-3119/
# https://www.geeksforgeeks.org/abstract-classes-in-python/#:~:text=An%20abstract%20class%20can%20be,is%20called%20an%20abstract%20class.

# SortedListAbc.py
# Appliance.py
# TextFilter.py
# Abstract.py

# 7. Multiple Inheritance
# Multiple inheritance is where one class inherits from two or more other classes. (already discussed)

# 8. Metaclasses *
# A metaclass is to a class what a class is to an instance; that is, a metaclass is used to create classes, just as classes are used to create instances. And just as we can ask whether an instance belongs to a class by using isinstance(), we can ask whether a class object (such as dict, int, or SortedList) inherits another class using issubclass(). The simplest use of metaclasses is to make custom classes fit into Python’s standard ABC hierarchy.
# https://www.geeksforgeeks.org/python-metaclasses/#:~:text=A%20metaclass%20is%20an%20efficient,look%20at%20the%20below%20code.


# 13. Functional-Style Programming
# Functional-style programming is an approach to programming where computations are built up from combining functions that don’t modify their args and that don’t refer to or change the program’s state, and that provide their results as return values. One strong appeal of this kind of programming is that (in theory), it is much easier to develop functions in isolation and to debug functional programs. This is helped by the fact that functional programs don’t have state changes, so it is possible to reason about their functions mathematically. Three concepts that are strongly associated with functional programming are mapping, filtering, and reducing.

item_list = [1, 2, 3, 4]

def process_item(x): return x*x
print(list(map(process_item, item_list)))	# [1, 4, 9, 16]
[x ** 2 for x in [1, 2, 3, 4]]			# list comprehension
(x ** 2 for x in [1, 2, 3, 4])			# iterator getting

def condition(x): return(x % 2 == 0)
print(list(filter(condition, item_list)))    	# [2, 4]
[x for x in [1, -2, 3, -4] if x > 0]

from functools import reduce	# also operator and itertools modules are useful
def add(a,b): return(a+b)
print(reduce(add, item_list))    # 10 (((1+2) + 3) + 4)

# Functions that use reduction (all, any, min, max, sum), there are lots of functions prepared already (or_, and_, etc.)

area = lambda b, h: 0.5 * b * h		# defining function that we use only once
def area(b, h): return 0.5 * b * h	# this is the same as the previous line

print(list(filter(lambda x: x % 3 == 0, range(16))))	# [0, 3, 6, 9, 12, 15]


# 1. Partial Function Application
# Partial function application is the creation of a function from an existing function and some args to produce a new function that does what the original function did, but with some args fixed so that callers don’t have to pass them. Here’s a very simple example:
enumerate1 = functools.partial(enumerate, start=1)
for lino, line in enumerate1(item_list):
    print(lino, line)

# 2. Coroutines *
# Coroutines are functions whose processing can be suspended and resumed at specific points. So, typically, a coroutine will execute up to a certain statement, then suspend execution while waiting for some data. At this point other parts of the program can continue to execute (usually other coroutines that aren’t suspended). Once the data is received the coroutine resumes from the point it was suspended, performs processing (presumably based on the data it got), and possibly sends its results to another coroutine. Coroutines are said to have multiple entry and exit points, since they can have more than one place where they suspend and resume.
# In Python, a coroutine is a function that takes its input from a yield expression.
# It may also send results to a receiver function (which itself must be a coroutine). Whenever a coroutine reaches a yield expression it suspends waiting for data; and once it receives data, it resumes execution from that point. A coroutine can have more than one yield expression.
# https://www.geeksforgeeks.org/coroutine-in-python/#:~:text=by%20the%20programmer.-,Python%20Coroutine,coroutines%20can%20also%20consume%20data.&text=whatever%20value%20we%20send%20to,returned%20by%20(yield)%20expression.

# 3. Performing Independent Actions on Data *
# If we want to perform a set of independent operations on some data, the conventional approach is to apply each operation in turn. The disadvantage of this is that if one of the operations is slow, the program as a whole must wait for the operation to complete before going on to the next one. A solution to this is to use coroutines. We can implement each operation as a coroutine and then start them all off. If one is slow it won’t affect the others—at least not until they run out of data to process—since they all operate independently. (more in book)
# https://www.geeksforgeeks.org/coroutine-in-python/


# 4. Composing Pipelines *
# Sometimes it is useful to create data processing pipelines. A pipeline is simply the composition of one or more functions where data items are sent to the first function, which then either discards the item (filters it out) or passes it on to the next function (either as is or transformed in some way). The second function receives the item from the first function and repeats the process, discarding or passing on the item (possibly transformed in a different way) to the next function, and so on. Items that reach the end are then output in some way.

# Valid.py


# Other
# SOME TIPS
A = 3; B = 4		# multiple statements in one line

print(1_000_000) 	# 1000000 	(decimal)
print(0b_1111_0000)	# 240		(binary)
print(0x_1234_abcd)	# 305441741	(hexadecimal)

# z = {**x, **y} 			# merges x and y dictionaries into z
# *_, paths = 2, 4, [2, 4]		# convention if you want only last returning value

# chr() - returns a character (a string) from an integer (represents unicode code point of the character) 
# ord() - given a string of length one, returns an integer representing the Unicode code point of the character when the arg is a unicode object, or the value of the byte when the arg is an 8-bit string.

# hasattr(object, name)	returns true if an object has the given named attribute and false if it does not
# iter(object, sentinel)	function returns an iterator for the given object 
# object - object whose iterator has to be created (can be sets, tuples, etc.)
# sentinel - special value that is used to represent the end of a sequence

# return NotImplemented	letting users know that certain function isn't done 
# special string characters "\N{SUPERSCRIPT TWO} \N{RIGHTWARDS ARROW}"

# modules for performance testing: 
# logging, timeit (small code snippets), cProfile (whole app)

# Example if we want to run evo.runEvolution(evo_parameters): cProfile.run("evo.runEvolution(evo_parameters)")

# performance solutions: Cython https://naucse.python.cz/course/mi-pyt/

# FORMATTING
print("{} {} {}".format("Python", "can", "count"))	# Python can count
print("{1}{0} is here".format("Paul", "Parker"))	# Parker Paul is here
print("{who} needs {amount} euro".format(amount=12, who="boy")) # boy needs 12 euro

stock = ['paper', 'sheet', 'pen']
print("We've got {0[1]} and {0[2]}".format(stock))	# We've got sheet and pen
# we can also access string keys in dicts or attributes via dot notation

print("{{{0}}} {1} ;-}}".format("With", "Without")) # {With} Without ;-}
    
# {0:25} 	- min length 25
# {0:>25} 	- right-alignment, min length 25
# {0:^25} 	- left-alignment, min length 25
# {0:-^25} 	- fill -, min length 25
# {0:-<25} 	- fill -, left-alignment, min length 25
# {0:.10} 	- max length 10
s = "Sword of truth"
print("{0:.{1}}".format(s, 11))        # Sword of tr

print("{0} subor{1}".format(
(count if count != 0 else "ziadny"),	  	# subor
("y" if count in range(2,5) else   		# subory
   	("" if count in range (0,2) else "ov"))))	# suborov 

# BIT OPERATIONS
print(5 >> 4)  	# 0 Right Shift 4 times	(101 -> 000)
print(5 << 1)  	# 10 Left Shift 1 time	(0101 -> 1010)
print(8 & 5)   	# 0 Bitwise AND 		(1000 & 0101 -> 0000)
print(9 | 4)   	# 13 Bitwise OR 		(1001 | 0100 -> 1101)
print(12 ^ 42) 	# 38 Bitwise XOR		(001100 ^ 101010 -> 100110)
print(~88)     	# -89 Bitwise NOT		(just adds negative -1)
print(~-88)  		# 87

print(0b1)   		# 1
print(0b10) 		# 2
print(0b11 & 0b10) 	# 2

print(bin(5))        # 0b101
print(int("111", 2)) # 7

# There’s also hex or oct (0o, 0x)

# NOTE: var names difference inside and outsides difference (context)
# NOTE: spaghetti code - function (multiple calls, parameter read, testing)

# Useful stuff:
# useful module: pickle (for storing variables), gzip (compressing/decompressing files)
# useful binary file methods: str.encode(), byte.decode(), bytearray(), bytes()
# https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc (underscores of Python)
# https://www.geeksforgeeks.org/try-except-vs-if-in-python/
# https://stackoverflow.com/questions/25030656/python-try-block-size

# I have the tools, I know how they work. The question is, when to use it?

