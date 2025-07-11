"""I am printing the hello world."""
print("hello world")

NAME="sohan"
AGE=20
print(f"hello {NAME}.My age is {AGE}")

A=3
B=2
SUM=A+B
print("The sum is",SUM)

a=12
b=16
for i in range(5):
 sums=a+b
 subract=a-b
 if(a>=10 and b>=10):
    print(sums)
    print("Addition sucessfully")
 else:
    print(subract)
    print("subraction successfully")

   
    
s={1,2,3,4}
print(s)

d=set()
d.add(5)
print(d)

s1={1,2,3}
s2={3,4,5}
print(s1.union(s2))
print(s1.intersection(s2))

#frozenset example
fs=frozenset([1,2,3,3,2])
print(fs)

s={frozenset([1,2]),frozenset([3,4])}
print(s)

from collections import defaultdict
d=defaultdict(int)
d['a']=1
print(d)

d2=defaultdict(list)
d2['x'].append(10)
print(d2)

try:
   num=int(input("enter a number"))
   result=10/num    
   print("Result is",result)
except ZeroDivisionError:
   
   print("cannot divide by zero")
except ValueError:
   print("invalid input,please enter a number")

import turtle
t=turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()
   
