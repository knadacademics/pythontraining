'''
Created on Dec 26, 2023

@author: kwabe
'''

''' functions '''

#creating the function
def my_function(x,y):
    return x + y

#using the function
print(my_function(3, 4))

result = my_function(7,8)
print(result)


#creating another function 
def function_without_return(x):
    print(x)
    
#using
result = function_without_return("hello!");

#doesn't have any return
print(result)



#function positional arguments

def my_function2(x,y,z=1.5):
    if z > 1:
        return z * (x+y)
    else:
        return z / (x+y)
    
#using the functions 
print(my_function2(5,6,z=0.7))
print(my_function2(3.14,7,3.5))
print(my_function2(10,10))


#function scope

a = []
def func():
    for i in range(5):
        a.append(i)
        
func()

print(a)

func()

print(a)

#another function
a = None 

def bind_a_variable():
    global a
    a = []
    
bind_a_variable()

print(a)    


def f():
    a = 5
    b = 6
    c = 7
    return a, b, c 

a, b,c = f() 

print(a,b,c)

# function are objects

def f1():
    a = 5
    b = 6
    c = 7
    return {"a":a, "b":b, "c":c}


print(f1())


#data transformation 

states = ["   Alabama ", "Georgia!", "Georgia", "georgia", "FlOrIda",
           "south   carolina##", "West virginia?"]


import re 

def clean_Strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub("[!#?]","",value)
        value = value.title()
        result.append(value)
        
    return result 

print(clean_Strings(states))


def remove_punctuation(value):
    return re.sub("[!#?]","",value)


clean_ops = [str.strip,remove_punctuation,str.title]


def clean_strings1(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
        
    return result 


print(clean_strings1(states, clean_ops))


for x in map(remove_punctuation,states):
    print(x)

print('here')
#Anonymous/Lambda functions

def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4,0,1,5,6]

print(apply_to_list(ints,lambda x: x * 2))

#sorting a collection of strings
strings = ["foo", "card", "bar", "aaaa", "abab"]

strings.sort(key=lambda x: len(set(x)))

print(strings)

some_dict = {"a":1, "b":2, "c":3}

for key in some_dict:
    print(key)

dict_iterator = iter(some_dict)

print(list(dict_iterator))


#generator square 
#use the yield keyword instead of return 

def square(n=10):
    print(f"Generating squares from 1 to {n**2}")
    for i in range(1,n+1):
        yield i**2
        
gen = square()

print(gen)

#getting values from gen
for x in gen:
    print(x, end=" ")
    

#using generator expressions
gen = (x ** 2 for x in range(100))

print(gen)

print(sum(x ** 2 for x in range(100)))

print(dict((i,i ** 2) for i in range(5)))

import itertools 

def first_letter(x):
    return x[0]

names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven"]

for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names is a generator


## ERRORS AND EXCEPTION HANDLING

def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x 
    
attempt_float("1.2334")
attempt_float("something")


##Files and the operating System

path = "segismundo.txt"

f = open(path, encoding="utf-8")

for line in f:
    print(line)
    

lines = [x.rstrip() for x in open(path, encoding="utf-8")]
print(lines)
f.close()

with open(path, encoding="utf-8") as f:
    lines = [x.rstrip() for x in f]

    



