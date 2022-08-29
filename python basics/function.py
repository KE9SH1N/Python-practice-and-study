#simple function syntex

def my_function():
  print("Hello from a function")


#Arguments


def my_function(fname):
  print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


#Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")





#def my_function(country = "Norway"):


def my_function(country= "Norway"):
  print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Return Values

def my_function(x):
  return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
