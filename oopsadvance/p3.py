class Parent:
    def sho(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

p = Parent()
p.sho()
c = Child()
c.sho()
c.show()
