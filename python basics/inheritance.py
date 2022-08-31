#inheritance 
#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:


x = Person("John", "Doe")
x.printname()

#pass keyword to make student class as person class
class Student(Person):
  pass


x = Student("Mike", "Olsen")
x.printname()


#Use the super() Function

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
