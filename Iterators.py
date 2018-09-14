# An iterator is an object that contains a countable number of values
# An iterator is an object that can be iterated upon
# In Python, an iterator implements the iterator protocol, this consists of the
# methods __iter__() and next()

# Lists, tuples, dictionaries and sets are all iterable objects.
# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings too

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#__________Create an Iterator_____________
# To create an object/class as an iterator you have to implement the methods
# __iter__() and __next__()
# the __iter__() initialize and you can do operations
# the __next__() also do operations, and must return the next item in the sequence

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Stop the Iteration
# This is used to prevent the iteration to go on forever in case of a loop

class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers1()
myiter = iter(myclass)

for z in myiter:
    print(z)