class Animal:
    def speak(self):
        return "Sound"
    
class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"
a = Animal()
print(f"Sound:  {a.speak()}")
d = Dog()
print(f"Sound:  {d.speak()}")
c = Cat()
print(f"Sound:  {c.speak()}")