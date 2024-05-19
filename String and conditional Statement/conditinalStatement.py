# Syntax: if-elif-else
'''
if(condition):
    Statement1
elif(condition):
    Statement2
else:
    Statement N

'''

age=23
if(age>=18):
    print("Now You can vote")

ligth="red"
if(ligth=="red"):
    print("Now you can wait for ligth green")
elif(ligth=="green"):
    print("Now you can go")
else:
    print("Go careful ")


# Provide a Grade student based on marks
mark=8

if(mark>=90):
    print("Grade A")
elif(90>=mark and mark>=80):
    print("Grade B")
elif(80>=mark and mark>=70):
    print("Grade C")
else:
    print("Grade D")



# Write a profram to check if a number entered ther user is odd or even in python
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")