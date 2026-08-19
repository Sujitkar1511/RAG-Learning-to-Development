class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    @staticmethod
    def Hello():
        print("Hello, I am a static method.")

s1 = Student("Sujit kar", 20)
s1.display()
Student.Hello()
