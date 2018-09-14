# A module is a code library
# Is a file containing a set of functions you want to include in your app

#Create a Module
# Create a file with the extension .py
def greeting(name):
    print("Hello, " + name)

#Use a Module
import mymodule
mymodule.greeting("jonathan")

#Rename a module
import mymodule as mx

#Built in modules
import platform

#List all the function names in a module
x = dir(platform)
print(x)

#importing only one function or variable froma a module
from mymodule import variable
