#1
a = int(input("Enter your age:"))
if (a>=18):
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")

#2
a = int(input("enter your marks:"))
if(a>=90):
    print("Your grade is A")
elif(a>=80 and a<90):{
    print("your grade is B")
}
else:{
    print("your grade is C")
}
    
#3
a=input("Enter the traffic light color:")
if(a=="red"):{
    print("stop")
}
elif(a=="yellow"):{
    print("Wait")
}
elif(a=="green"):{
    print("Go")
}

#4
balance = 1000
a = int(input("Enter the amount which you want to withdraw"))
if ((balance-a)>0):{
    print("sufficient balance")
}
else:{
    print("insufficient balance")
}

#5
a = int(input("Enter your number:"))
if(a>0):{
    print("the number is positive")
}
elif(a==0):{
    print("The number is zero")
}
else:{
    print("The number is negative")
}

#6
a = int(input("enter your number to check if it lies between 1 to 100"))
if(a>1 and a<100):{
    print("Your number lies in the range")
}
else:{
    print("Your number doesn't lie in this range")
}
    
#7
user= "name"
pas = 123
u = input("enter the username")
p = int(input("enter the password"))
if(u==user and pas ==p):{
    print("Your user & pass is verfied")
}
else:{
    print("your user & pass is not verfied")
}

#8
unit = 20
u = int(input("enter the number of units used"))
print("The total electricity bill is:",u*unit)

#9
a = int(input("Enter first number"))
b = int(input("Enter second number"))
print("Enter a for addition")
print("Enter s for subtraction")
print("Enter m for multiplication")
print("Enter d for divide")
c = input("enter the letter which you want to perform")
if(c=="a"):{
    print("Addition:",a+b)
}
elif(c=="s"):{
    print("Subtraction:",a-b)
}
elif(c=="m"):{
    print("Multiplicaiton:",a*b)
}
elif(c=="d"):{
    print("Division:",a/b)
}

#10
a = int(input("Enter first sides of triangle:"))
b = int(input("Enter seconnd sides of triangle:"))
c = int(input("Enter third sides of triangle:"))
if(a==b and b==c):{
    print("It is an equilateral triangle")
}
elif(a!=b and b!=c):{
    print("It is an Scalene triangle")
}
elif(a==b or b==c):{
    print("it is an isosceles triangle")
}

#OUTPUT
"""
Enter your age:19
You are eligible for vote
enter your marks:88
your grade is B
Enter the traffic light color:red
stop
Enter the amount which you want to withdraw800
sufficient balance
Enter your number:19
the number is positive
enter your number to check if it lies between 1 to 10099
Your number lies in the range
enter the usernamehello
enter the password123
your user & pass is not verfied
enter the number of units used30
The total electricity bill is: 600
Enter first number18
Enter second number49
Enter a for addition
Enter s for subtraction
Enter m for multiplication
Enter d for divide
enter the letter which you want to performa
Addition: 67
Enter first sides of triangle:13
Enter seconnd sides of triangle:13
Enter third sides of triangle:13
It is an equilateral triangle
"""