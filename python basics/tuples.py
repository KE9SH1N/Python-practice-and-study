#tuples can not be changed like list
#syntex also different
#tuple allow duplicates item

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#one item tuple
#one , is the key point


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#tuple data type

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

print(tuple1, tuple2, tuple3)
#mixed data type
print(tuple4)

#tuple() method

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


#Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#if else in tuple

thistuple = ("apple", "banana", "cherry")
if "apples" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

else:
    print("N\A")


#Update Tuples
#Change Tuple Values
#we need to change a tuple to a list first then we can update any value on it

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#add item

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#we can add 2 tuple into a tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#Unpacking a tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Using Asterisk * to create a list


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#loop tuples

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#join tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#count method for tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

#index method for tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
