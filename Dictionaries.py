# A dictionary is a collection which is unordered, changeable and indexed.

thisDict = {
    "apple": "green",
    "bannana": "yellow",
    "cherry": "red"
}
print(thisDict)

#Changing elements
thisDict["apple"] = "red"
print(thisDict)

#Create dictionary with method
thisdict = dict(apple="green", bannana="yellow", cherry="red")
print(thisdict)

#adding items
thisdict["damson"] = "purple"
print(thisdict)

#deleting items
del(thisdict["bannana"])
print(thisdict)