# String  is a data types that stores a sequence of character
# In python there are three way define string and all is valid
str1="Vishal Pal"
str2='Lucknow'
str3='''Uttar Pradesh'''
str4="vishal"
print(str1)
print(str2)
print(str3)


# String concatenation
print(str1+" "+str2+" "+str3)

# find the length of the any string
print("Length of the: ", len(str3))    #whitespace is also count one 

# Indexes of string
print(str1[9])

# Slicing string   Syntax : str[starting_indx : ending_indx]
print(str2[1:5])


# Practice some string functions
print(str1.endswith("al")) #return true if string end with substr
print(str4.capitalize()) #Capitalize 1st char in string
print(str4.replace("v","B")) # Replace all occurances
print(str3.find("tt")) # return 1st index of 1st occurance. If find(1) else (-1)
print(str3.count("t")) # Count thee occcurnce of substr in string



# WAP to input user's first name & print the length
first=input("Enter the first name:")
print("Total length of your first name: ",len(first))


# WAP to find the occurance of $ in a string
str5="I am vishalpla$@gmail.com"
print("Firts occurance and  index number: ",str5.find("$"))
