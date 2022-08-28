#length of the list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))



#string int boolean list

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1, list2, list3)

#all data types in a list

list4 = ["abc", 34, True, 40, "male"]

print(list4)

#type

print(type(list4))

#access list

# list() constructor making a new list and round brackets instead of 3rd brackets
newlist = list(("apple", "banana", "cherry"))
print(newlist)

#returning the specific index range value

newlist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(newlist2[2:5])

#changing list vlaue

#here banana will changed to blackcurrant
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#insert a new item 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#append method

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#extend method

#to add item from another list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove from list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

#remove specific item from a list
thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)


#for loop in list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#while loop in list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1




#list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



#sort list but sort always case sensitive

thislist = ["orange", "Mango", "kiwi", "pineapple", "banana"]
numberlist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
numberlist.sort()
print(numberlist)


#case sensitive sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)


#reverse method

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#copy a list

#copy() list() are same even we can use = sign only

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print(thislist)


#join list
#using extend method 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#using append method

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#using concatenation + sign

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#clear the entire list we can use clear method
mylist = mylist.clear()
print('#')
print(mylist)


# The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. 
# This means that tuples cannot be changed while the lists can be modified. Tuples are more memory efficient than the lists.
