# Lambda is a small anonymoud function
# This function can take any number of arguments, but can only have one
# expression

# Lambda function that adds 10 to the number passed in as an argument
x = lambda a:a + 10
print(x(5))

y = lambda a, b:a * b
print(y(5,6))

def my_func(n):
    return lambda a:a * n

mydoubler = my_func(2)

print(mydoubler(10))