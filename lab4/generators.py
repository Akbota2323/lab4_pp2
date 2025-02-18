def numbers(a):
    for i in range(a+1):
        yield i * i
        
for number in numbers(5):
    print(number)
    
#2
def numbers(a):
    for x in range(a+1):
        yield x
for x in range(8):
    if x%2==0 and x!=0:
        print(x,end=',')
        
#3
def numbers(a):
    for x in range(a+1):
        yield x
for x in range(24):
    if x%3==0 and x%4==0 and x!=0:
        print(x)

#4
def squares(a,b):
    for i in range(a,b+1):
        yield i * i
        
for square in squares(1,6):
    print(square)

#5
def numbers(a,b,c):
    for i in range(a,b,c):
        yield i 
        
for number in numbers(6,0,-1):
    print(number)