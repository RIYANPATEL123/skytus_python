class Student:
    def __init__(self,maths,science,cs):
        self.maths = maths
        self.science = science
        self.cs = cs

    def avg(self):
        a = (self.maths + self.science + self.cs)/3
        return a

s = Student(80,90,70)
print(f"Student marks in marths {s.maths}")
print(f"Student marks in science {s.science}")
print(f"Student marks in cs {s.cs}")

print(f"Averge marks {s.avg()}")
