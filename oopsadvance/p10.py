class Parent:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"The name is {self.name}")
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def display(self):
        print(f"The name is {self.name} and the age is {self.age}")

p = Parent("Hello")
p.display()
c = Child("RIyan",20)
c.display()