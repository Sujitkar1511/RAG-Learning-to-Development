class Student:
    def __init__(self,name,rollNo,marks):
        self.name=name
        self.rollNo=rollNo
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rollNo)
        print("Marks:",self.marks)


s1=Student("Sujit kar", 101, 95)
s1.display()