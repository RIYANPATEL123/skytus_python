class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        a = 22*(self.radius**2)/7
        print(f"The area of the circle is {a}")
    
    def circumference(self):
        a = 2 *22*self.radius/7
        print(f"the circumferrence of the circle is {a}")
    
c = Circle(7)
c.area()
c.circumference()
