#Creating a function


def my_function():
    print("Hello from my Function")

#Calling a function
my_function()

#Parameters


def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

#Default parameter value


def my_function0(country = "Norway"):
    print("I am from " + country)

my_function0("Sweden")
my_function0("India")
my_function0()
my_function0("Brazil")

#Return Values


def my_function2(x):
    return 5 * x
print(my_function2(3))
print(my_function2(5))
print(my_function2(9))

