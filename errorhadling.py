#1
try:
    num=5/0
except ZeroDivisionError:
    print("a number cannot be divided by zero")

#2
try:
    a =int(input("Enter your age"))
    print("your age is",a)
except ValueError:
    print("Error: enter a valid integer")

#3
try:
    file = open("hello.txt",'r')
    f = file.read()
    f.close()
except FileNotFoundError:
    print("The file in note there at the location")

#4

try:
    num = 5/0
    a = int(input("enter your age"))
    print("your age",a)
    file = open("hello.txt",'r')
    f = f.read()
    f.close()

except ZeroDivisionError:
    print("number cannot be divided by zero")
except ValueError:
    print("Enter correct value")
except FileNotFoundError:
    print("file not in that location")
except Exception as e:
    print("The error occured is",e)

#5
try:
    num = 7/ 0
except ZeroDivisionError:
    print("Error")
finally:
    print("Program Ended")
#6
class InvalidAgeError(Exception):
    pass

age = -10
try:
    if age<0:
        raise InvalidAgeError("Age cannot be negative")
except InvalidAgeError as e:
    print(e)

#7
list = [14,52,13]
try:
    print(a[5])
except IndexError:
    print("The index is out of range")

#8
try:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    c = a/b
except ValueError:
    print("Enter correct value")
except ZeroDivisionError:
    print("number cannot be divided by zero")
except Exception as e:
    print("The error occured is",e)

#9
try:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    c = a/b
    print(c)
except ZeroDivisionError:
    file = open("hello.txt",'a')
    file.write("ZeroDivisionError occured")
    file.close()

#10
class InvalidEmailFormat(Exception):
    pass

try:
    a = input("Enter you email")
    if '@' not in a:
        raise InvalidEmailFormat("@ is not present")
    if '.' not in a:
        raise InvalidEmailFormat(". not present ")
    print(a)

except InvalidEmailFormat as e:
    print(e)



