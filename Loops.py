#______________________while Loops______________________________________
i = 1
while i < 6:
    print(i)
    i += 1

# break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#continue statement (Stops the current iteration and continue the next)
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#____________For Loops_____________________________________

fruits = ["apple", "bannana", "cherry"]
for x in fruits:
    print(x)

#break statement
for x in fruits:
    if x == "bannana":
        break
    print(x)

#continue statement
for x in fruits:
    if x == "bannana":
        continue
    print(x)

#range function returns a sequence of numbers, starting from 0 by default and
#increments by 1, ends at a specified number
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)
# range increments in 1 by default, with the third parameter ypu can change
#this
for x in range(2, 30, 3):
    print(x)

#Recursion. A function that calls himself
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Reults")
tri_recursion(6)
