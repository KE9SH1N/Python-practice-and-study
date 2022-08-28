a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(10 > 9)
print(10 == 9)
print(10 < 9)

#function can return boolean values
def myFunction():
  return False


if myFunction():
  print("YES!")
else:
  print("NO!")


#checking an object that is integer or not
x = 200
print(isinstance(x, int))
