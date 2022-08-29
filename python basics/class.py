#Create a Class

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


#The __init__() Function

#The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#Let us create a method in the Person class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

#update value
p1.age = 40

#delete value
del p1.age

#Delete Objects
del p1


