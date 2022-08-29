#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


#Duplicates Not Allowed
#Duplicate values will overwrite existing values

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)


#Accessing Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

#using get method

x = thisdict.get("model")

#keys value
x = thisdict.keys()


#adding a new item to a dictionary


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


#Change Values

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018


#Update Dictionary
#update method

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})


#Removing Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#pop item  method remove last inserted item

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

#delete dictionary
#del keyword

#clear method can empties the dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)


#loop dictionary

for x in thisdict:
  print(x)



#values

for x in thisdict.values():
  print(x)

#keys

for x in thisdict.keys():
  print(x)

#items


for x, y in thisdict.items():
  print(x, y)


#copy method and dict function are same

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#difference between function and method in python
#Functions can be called only by its name, as it is defined independently. 
# But methods can't be called by its name only, we need to invoke the class by a reference of that class in which it is defined, 
# i.e. method is defined within a class and hence they are dependent on that class.


#Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

