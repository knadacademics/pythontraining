'''
Created on Dec 20, 2023

@author: kwabe
'''

from supervisedLearning.new_module import g, PI 

if __name__ == '__main__':
    pass

a = 5; b=4.5

#checking the type of a variable
print(isinstance(a,(int, float)))

#using import
result = g(5,PI)


#basic arithmetic statements
print(5//2)
print(5**2)

a = [1,2,3]

b = a 

c = list(a)

print(a is b)

#mutable objects a list is mutable
a_list = ["foo",2,[4,5]]

a_list[2] = (3,4)

print(a_list)

#immutable, a tuple is NOT mutable
a_tuple = (3,5,(4,5))

#a_tuple[1] = "four"

print(a is not c)

#handling scalar types


#numeric types
ival = 17239871

print(ival ** 6)

fval = 7.243
fval2 = 6.78e-5

#string type

c = """
    This is a longer string that
    spans multiple lines
    """

print(c.count("\n"))

s = 'python'

list(s)

print(list(s))

print(s[:3])

print("12\\34")

s = r"this\has\no\special\characters"

print(s)

template = "{0:.2f} {1:s} are worth US${2:d}"

print(template.format(88.46,"Argentina Pesos",1))

amount = 10

rate = 88.46

currency = "Pesos"

result = f"{amount} {currency} is worth US${amount/rate:.2f}"

print(result)

#working with dates and time

from datetime import datetime, date, time 

dt = datetime(2011,10,29,20,30,21)

print(dt.day)

print(dt.minute)

print(dt.date())

print(dt.time())

print(dt.strftime("%Y-%m-%d %H:%M"))

print(datetime.strptime("20091031", "%Y%m%d"))
