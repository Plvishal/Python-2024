# Loops are used to repeat instructions
# In python there are two types of loops
# 1.While Loop
# 2. For Loop


# 1. Print numbers from 1 to 100
num=1
while num<=100:
    print(num)
    num+=1
# 2. Print number from 100 to 1
num1=100
while num1>=1:
    print(num1)
    num1-=1

# 3. Print the multification table of a number n

# n=int(input("Enter a number: "))
# i=1
# while i<=10:
#     print( i*n)
#     i+=1

print("*****************")
# Print the element of the following list using a loop.
list=[1,4,9,16,25,36,49,64,81,100]

j=0
while j < len(list):
    print(list[j])
    j+=1
# Search for a numbers x in this tuple using loop:
x=(1,4,9,16,25,36,49,64,81,100)

a=0
y=100

while a < len(x):
    if x[a] == y:
        print("Number is find: ", x[a]," On index: ",a)
    a+=1

