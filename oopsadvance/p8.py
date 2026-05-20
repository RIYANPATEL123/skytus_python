class Teacher:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def teacher(self):
        print(f"The teacher name is {self.name} and age is {self.age}")
    
class Student(Teacher):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno = rollno
    
    def student(self):
        print(f"The student name is {self.name} age is {self.age} rollno is {self.rollno}")
    
t = Teacher("Skytus",30)
t.teacher()
s = Student("Riyan",19,101)
s.student()
