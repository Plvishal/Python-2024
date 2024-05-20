# A built-in data typrd that stores set of value
# List are mutable
# It can store all types(integers, float, string etc)

marks=[95,54,96.5 ,25 ,"Vishal"]
print(marks)

print(type(marks))
# SLicing
print(marks[2:4])

# List all method
a=[2,1,9,6,3,4,7]
a.append(8) # Adds one elements at the end
print(a)

# Sort
a.sort() #Sort in ascending order
print(a)

a.sort(reverse=True)  #sort in decending order
print(a)

# Reverse the list
a.reverse()
print(a)

# Insert element in list with index and element
a.insert(2,10) # insert element at the index (index,element)
print(a)

# Remove element from the List
a.remove(10) # remove the first occurrence of the element
print(a)


# Remove element by using the index
a.pop(1)
print(a)


