# A class with a property
class MyClass:
    x = 5

#create an object
p1 = MyClass()
print(p1.x)

#A class with a function and a function __init__()
# It's like a constructor of an object'
#The self variable is a reference to the class itself
class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("John", 36)
print(p1.name)
print(p1.age)

#Delete an object property
del p1.age

#Delete an object
del p1


