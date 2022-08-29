#Set

#set item Unordered, Unchangeable, Duplicates Not Allowed

thisset = {"apple", "banana", "cherry"}
print(thisset)


#Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


#Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

print(set4)


#set method for creating a set

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)


#Access Items of a set

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#set update method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#we can add an entire list to a set

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#set remvoe method

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


#set discard method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#set pop method for removing the last item of a set

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#set clear method

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#delete a set 

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)




#loop in a set

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Join Two Sets
#using union method
#The union() method returns a new set with all items from both sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#The update() method inserts the items in set2 into set1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


