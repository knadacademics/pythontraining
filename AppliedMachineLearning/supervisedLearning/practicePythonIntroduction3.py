#tuples

tup = (4,5,6)
print(tup)

print(tuple([4,0,2]))

#passing a string
tup = tuple('string')
print(tup)

#nested_tup
nested_tup = (4,5,6),(7,8)
print(nested_tup)

print(nested_tup[0])

tup = tuple(['foo',[1,2],True])

#unpacking tuples
tup = (4,5,6)

a,b,c = tup 

print(a)
print(b)
print(c)


tup = 4,5,(6,7)

a,b,(c,d) = tup 

print(d)


#using unpack in loops

seq = [(1,2,3),(4,5,6),(7,8,9)]

for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')
    

#another unpack
values = 1,2,3,4,5 
a,b, *_ = values 

print(a)
print(b)

#counting values in tuples 
a = (1,2,2,2,3,4,2)

print(a.count(2))

#working with list
a_list = [2,3,4,None]

tup = ("foo","bar","baz")

b_list = list(tup)
b_list[1]= "peekaboo"

b_list.append("dwarf")

b_list.insert(1, "red")

print(b_list)

#concatenating multiple lists
x = [4, None, "food"]
x.extend([7,8,(2,3)])
print(x)

#sorting
a = [7, 2, 5, 1, 3]
a.sort()
print(a)

b = ["saw", "small", "He", "foxes", "six"]
b.sort(key=len)
print("\n")

print("sorting by length")
print(b)
 
#slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5])


#assigning a slice
seq[3:5] = [6,3]
print(seq)

print(seq[:5])
print(seq[3:])
print(seq[-4:])
print(seq[-6:-2])
print(seq[::2])

# dictionary
empty_dict = {} #This is how to create an empy dictionary

d1 = {"a":"some value","b":[1,2,3,4]}

d1[7] = ["an float"]

print(d1["b"])

#checking for dictionary
print("b" in d1)


d1[5] = "some value"

del d1[5]

print(d1)

print("keys")
print(list(d1.keys()))
      
print("values")
print(list(d1.values()))

print("items")
print(list(d1.items()))


#updating a dictionary
d1.update({"b": "foo","c": 12})
print(d1)

#creating a dictionary from sequence
tuples = zip(range(5),reversed(range(5)))

print(tuples)

mapping = dict(tuples)

print(mapping)


#using default values in 
words = ["apple","bat","bar","atom","book"]

# by_letter = {}
#
# for word in words:
#     letter = word[0]
#     if letter not in by_letter:
#         by_letter[letter]= [word]
#     else:
#         by_letter[letter].append(word)
by_letter = {}

for word in words:
    letter = word[0]
    by_letter.setdefault(letter,[]).append(word)
    
    
#collections
from collections import defaultdict

by_letter = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)
    

#using set
print(set([2,3,4,5,5]))

a = {1,2,3,4,5}

b = {3,4,5,6,7,8}


#union operation
print(a.union(b))
print(a|b)

#intersection operation
print(a.intersection(b))
print(a&b)


my_data = [1,2,3,4]

my_set = {tuple(my_data)}

print(my_set)

#checking subset
a_set = {1,2,3,4,5}

print({1,2,3}.issubset(a_set))


#enumerate

# index = 0
# for value in collection:
#     #do something
#     index+=1

# for index, value in enumerate(collection):
#     #do something with value


#sorted
print(sorted([7,1,2,6,0,3,2]))

print(sorted("horse race"))


#zip
seq1 = ["foo", "bar", "barz"]
seq2 = ["one", "two", "three"]

seq3 = [False, True]

zipped = zip(seq1,seq2, seq3)

print(list(zipped))

#common use of zip
for index,(a,b) in enumerate(zip(seq1,seq2)):
    print(f'{index}:{a}, {b}')


#reversed
print(list(reversed(range(10))))


#list,set and dictionary comprehensions

#[expr for value in collection if condition]
strings = ["a", "as", "bat", "car", "dove", "python"]

results = [x.upper() for x in strings if len(x) > 2]

print(results)

#set_comprehension
unique_lengths = {len(x) for x in strings}

print(unique_lengths)

#functional way of doing it
print(set(map(len,strings)))


#dictionary comprehensions
loc_mapping = {value:index for index, value in enumerate(strings)}

print(loc_mapping)


#nested comprehensions
all_data = [["John", "Emily", "Michael", "Mary", "Steven"],
              ["Maria", "Juan", "Javier", "Natalia", "Pilar"]]

names_of_interest = []

for names in all_data:
    enough_as = [name for name in names if name.count("a")>=2]
    names_of_interest.extend(enough_as)
    
print(names_of_interest)

#compacted form 
result = [name for names in all_data 
          for name in names if name.count("a")>=2]
print(result)


#mine
result = []
for names in all_data:
    for name in names:
        if name.count("a") >= 2:
            result.append(name)

print(result)

#another example

some_tuples = [(1,2,3),(4,5,6),(7,8,9)]

flattened = [x for tup in some_tuples for x in tup]

print(flattened)


#list of list example
print([[x for x in tup] for tup in some_tuples])

