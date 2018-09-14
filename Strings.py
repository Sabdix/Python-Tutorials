#This is a comment in python

#Returns the character at position 1
a = "Hello, World"
print(a[1])

#Returns the characters from position 2 to 5
b = "Hello, World!"
print(b[2:5])

#Deletes the white spaces
#at the beginning and end of the string
a = " Hello, World! "
print(a.strip())

 #Returns the length of the String
a = "Hello, World!"
print(len(a))

#Returns the string in lower case
a = "Hello, World!"
print(a.lower())

#Returns the string in upper case
a = "Hello, World!"
print(a.upper())

#Replace the stirng with another string
a = "Hello, World!"
print(a.replace("H", "J"))

#Return the string split into substrings if it finds
#instances of the separator
a = "Hello, World!"
print(a.split(","))

#Expects an input from keyboard
print("Enter your name:")
x = input()
print("Hello, " + x)