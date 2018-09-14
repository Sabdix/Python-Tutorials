###_________Lists___________________________________

#Create List
thisList = ["apple", "bannana", "cherry"]
print(thisList)

#Change the second item
thisList[1] = "blackcurrant"
print(thisList)

#append() adds an element at the end of the list
thisList.append("pea")
print(thisList)

#copy() returns a copy of the list
x = thisList.copy()
print(x)

#count() returns the number of elements with the specified value
print(thisList.count("pea"))

#extend() Add the elements of a list to the end of the current list
thisList2 = ["pineapple", "watermellon", "mellon"]
thisList.extend(thisList2)
print(thisList)

#index() returns the index of the first element with the specified value
print(thisList.index("pea"))

#insert() adds an element at the specified position
thisList.insert(1, "orange")
print(thisList)

#pop() removes the element at the specified position
thisList.pop(1)
print(thisList)

#remove() removes the first item with the specified value
thisList.remove("mellon")
print(thisList)

#reverse() reverses the order of the list
thisList.reverse()
print(thisList)

#sort() sorts the list
thisList.sort()
print(thisList)

#clear() removes all the elements from the list
thisList.clear()
print(thisList)

#___________________List Constructor_________________________________
listConstructor = list(("apple", "bannana", "cherry"))
print(listConstructor)

#Append = add a item to the list
listConstructor.append("damson")
print(listConstructor)

#Remove = removes an item of the list
listConstructor.remove("bannana")
print(listConstructor)

#Len = returns the number of items of the list
print(len(listConstructor))