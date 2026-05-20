#1
def name():
    print("Riyan, 19years, valsad")

#2
def sum(a,b):
    print("The sum of the two number is:",a+b)

#3
def celToFah(a):
    a = (a*9/5)+32
    print("Converting celcius to Fahrenheit:",a)

#4
def upp():
    a = "riyan"
    print(a.upper())

#5
def birth(a):
    b = 2026
    print("Your age is:",b-a)

#6
def swap(a,b):
    c = a
    a = b
    b = c
    print("After swapping numbetrs:",a,b)

#7
def area(a,b):
    c= a*b
    print("area of the rectangle:",c)

#8
def positiv(a):
    if(a>0):{
        print("Positive")
    }
    else:{
        print("Negative")
    }
    
#9
def avg(a,b):
    print("Average:",(a+b)/2)

name()
print("Give first number for sum")
a=int(input())
print("Give Second number for sum")
b=int(input())
sum(a,b)
c = 38
celToFah(c)
upp()
d = 2006
birth(d)
swap(a,b)
area(a,b)
positiv(a)
avg(a,b)

