#1
for i in range(1,11):
    print(i)

#2
a = int(input("Enter the number for the multiplication table: "))
for i in range(1,11):
    print(a,"x",i,"=",a*i)

#3
fact = 1
for i in range(1,a+1):
    fact = fact*i

print("The factorial of number",a,"is",fact)

#4
print("Fibonacci series")
n = 10
a = 0
b = 1
for i in range(n):
    print(a)
    a = b
    b = a+b

#5
n = 17
b = True
if n<=1:
    b = False
else:
    for i in range(2,n):
        if n%i==0:
            b = False
            break
        else:
            b = True

if b:
    print("Prime")
else:
    print("Not prime")

#6
n = 123
print("reversed number:",int(str(n)[::-1]))

#7
c = 0
while(n>0):
    c = c+1
    n = n//10

print("the numeber of digits:",c)

#8
sum = 0
for i in range(2,101,2):
    sum +=i
print(sum)

#9
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    
    for k in range(2*i-1):
        print("*",end="")
    print()

#10
print("divisor of n")
for i in range(1,n+1):
    if(n%i==0):
        print(i)

#OUTPUT
"""
1
2
3
4
5
6
7
8
9
10
Enter the number for the multiplication table: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
The factorial of number 7 is 5040
Fibonacci series
0
1
2
4
8
16
32
64
128
256
Prime
reversed number: 321
the numeber of digits: 3
2550
    *
   ***
  *****
 *******
*********
divisor of n
1
5
"""