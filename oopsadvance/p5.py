
class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 4 * 4

def area(shape):
    print(shape.area())

c = Circle()
s = Square()
area(c)
area(s)