# Write a program to ask the user to enter names of thier's 3 favorite movies and store themm in a list
movies=[]
m1=input("enter your first movie: ")
m2=input("enter your second movie")
m3=input("enter your third movie: ")
movies.append(m1)
movies.append(m2)
movies.append(m3)

print(movies)


# Write a program to check if a list contains a palindrome of element(Hint:  use copy method)
list1=[1,2,1]
list2=list1.copy()
list2.reverse()
print(list2)
if(list1==list2):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
