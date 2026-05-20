class Rectangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base*self.height
    
    def perimeter(self):
        return 2*(self.base+self.height)
    
r = Rectangle(8,4)
print(f"The base of the rectangle {r.base}")
print(f"The height of the rectangle {r.height}")

print(f"The area of rectangle {r.area()}")

print(f"The perimeter of rectangle {r.perimeter()}")