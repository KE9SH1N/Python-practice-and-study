#try except

try:
  print(x)
except:
  print("An exception occurred")

#Print one message if the try block raises a NameError and another for other errors
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



#else
#In this example, the try block does not generate any error
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#finally
#The finally block, if specified, will be executed regardless if the try block raises an error or not

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
