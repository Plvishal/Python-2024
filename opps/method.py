class Student:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def welcome(self):
        print("Welcome Student", self.name,self.age)
s1=Student("Vishal",23)
s1.welcome()