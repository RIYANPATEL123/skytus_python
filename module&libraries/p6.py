from shapes import circle
from shapes import rectangle
a = int(input("enter radius of circle"))
print(f"Area: {circle.area(a)}")
print(f"Circumference: {circle.circumfarence(a)}")

a = int(input("Enter base of rectangle"))
b = int(input("Enter height of rectangle"))
print(f"Area: {rectangle.area(a,b)}")
print(f"perimeter: {rectangle.perimeter(a,b)}")
