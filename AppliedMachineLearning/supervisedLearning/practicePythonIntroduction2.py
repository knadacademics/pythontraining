#control flow

x = -5 
if x < 0:
    print("It's a negative")
elif x == 0:
    print("Equal to Zero")
elif 0 < x < 5:
    print("Positive but simpler than 5")
else:
    print("Positive and larger than or equal to 5")

    
    
#for loops
sequence = [1,2, None, 4, None,5]
total = 0

for value in sequence:
    if value is None:
        continue
    total+=value 
    
print(total)


sequence = [1,2,0,4,6,5,2,1]
total_unit_5 = 0

for value in sequence:
    if value == 5:
        break 
    total_unit_5+=value 
    
    
print(total_unit_5)



for i in range(4):
    for j in range(4):
        if j > i:
            break
        print(i,j)
        
#while loops 
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x 
    print(x//2) 


print(list(range(10)))
print(list(range(0,20,2)))
print(list(range(5,0,-1)))


seq = [1,2,3,4]

for i in range(len(seq)):
    print(f"element {i}: {seq[i]}")
    

total = 0

for i in range(100_000):
    # % is a modulo operator
    if i % 3 ==0 or i % 5 == 0:
        total += i 
    
print(total)
    
