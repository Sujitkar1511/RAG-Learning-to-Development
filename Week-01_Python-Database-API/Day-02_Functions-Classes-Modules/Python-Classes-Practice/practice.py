class Student:
    def __init__(self,name,sub1,marks):
        self.name=name

        sum=0;
        for mark in marks:
            sum+=mark  
        self.marks=sum

    def display(self):
        print("Name:",self.name)
        print("Total Marks:",self.marks)    

s1=Student("Sujit kar", 101, [95, 90, 85])
s1.display()

       