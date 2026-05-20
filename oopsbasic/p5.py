class Employee:
    def __init__(self,salary):
        self.salary = salary
    
    def display(self):
        print(f"The salary is:",self.salary)
    
e = Employee(10000)
e.display()
