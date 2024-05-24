

class Student:
    # Default parameter 
    def __init__(self):
        print("Default Constructor")
        # Parameterised Constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print('Parameterised Co')
s1=Student("Vishal Pal",34)
print(s1.name)
