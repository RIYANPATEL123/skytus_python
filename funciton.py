def prime():
    n = 17
    b = True
    if n<=1:
        b = False
    else:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                b = False
                break
            else:
                b = True
    return b

def rev():
    a = input("Enter the string to be reverserd")
    print("the reversed string:",a[::-1])



def fact(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact*i
    print("The factorial of number",a,"is",fact)

def cal():
    p = 1000
    r = 10
    t = 2
    si = p*r*t/100
    print("The simple interest is:",si)

def pali():
    a = input("Enter a string to check if it is palindrome or not")
    b = a[::-1]
    if(a==b):{
        print("the string is palindrome")
    }
    else:{
        print("The string is not palindrome")
    }

def vow():
    a = input("enter the string to count vowels")
    v = ["a","e","i","o","u","A","E","I","O","U"]
    c = 0
    for i in a:
        if i in v:
            c = c+1
        
    print("The no of vowels in:",a,"is",c)

def mer():
    l1 = [1,4,6,2]
    l2 = [6,3,8,9]
    m = l1 +l2
    print("the merged list is",m)

def gcd():
    a = int(input("Enter the first number to find the gcd"))
    b = int(input("Enter the second number to find gcd"))
    while(b!=0):
        a,b = b,a%b
    print("The gcd of two number is:",a)


def area():
    a = int(input("Enter the base of rectangle"))
    b = int(input("Enter the height of the rectangle"))
    c= a*b
    print("area of the rectangle:",c)

def armstrong():
    a = int(input("Enter the number to check if it is an armstrong number or not"))
    c = len(str(a))
    d = 0
    for i in str(a):
        d += int(i)**c
    if d == a:
        print("the number is armstrong")
    else:
        print("the number is not armstrong")



if prime():
    print("Prime")
else:
    print("NOt prime")
rev()
a = int(input("enter the a number for factorial"))
fact(a)
cal()
pali()
vow()
mer()
gcd()
area()
armstrong()

#OUTPUT
"""
Prime
Enter the string to be reverserdhello
the reversed string: olleh
enter the a number for factorial5
The factorial of number 5 is 120
The simple interest is: 200.0
Enter a string to check if it is palindrome or nothelleh
the string is palindrome
enter the string to count vowelsHelloI
The no of vowels in: HelloI is 3
the merged list is [1, 4, 6, 2, 6, 3, 8, 9]
Enter the first number to find the gcd14
Enter the second number to find gcd16
The gcd of two number is: 2
Enter the base of rectangle4
Enter the height of the rectangle5
area of the rectangle: 20
Enter the number to check if it is an armstrong number or not123
"""