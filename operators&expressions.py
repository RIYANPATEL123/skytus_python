#1
def remainder(a,b):
    c = a%b
    print("The remainder of two number is: ",c)

#2
def evenOrOdd(a):
    if(a%2==0):{
        print("The number even is:",a)
    }
    else:{
        print("The number odd is:",a)
    }

#3
def larger(a,b):
    if(a>b):{
        print("The number Larger is:",a)
    }
    else:{
        print("The number Larger is:",b)
    }

#4
def squareAndCube(a):
    print("The square of number is:",a**2)
    print("The cube of number is:",a**3)

#5
def equal(a,b):
    if(a==b):{
        print("Both the number are equal")
    }
    else:{
        print("The numbers are not equal")
    }

#6
def positiv(a,b):
    if(a>0 and b>0):{
        print("True")
    }
    else:{
        print("False")
    }

#7
def floatToInteger(a):
    c = int(a)
    print(c)
#8
def stri(a):
    c = int(a)
    c = c*10
    print(c)

#9
def multipleConditions(a,b):
    if(a>b and b>0):{
        print("a is a positive number as b>0")
    }

#10
def quoAndRemi(a,b):
    c = a//b
    d = a%b
    print("The quotient is:",c)
    print("The remainder is:",d)

a = 10
b = 8
remainder(a,b)
evenOrOdd(a)
larger(a,b)
squareAndCube(a)
equal(a,b)
positiv(a,b)
c = 15.0
floatToInteger(c)
stri(str(a))
multipleConditions(a,b)
quoAndRemi(a,b)

#OUTPUT
"""
The remainder of two number is:  2
The number even is: 10
The number Larger is: 10
The square of number is: 100
The cube of number is: 1000
The numbers are not equal
True
15
100
a is a positive number as b>0
The quotient is: 1
The remainder is: 2
"""