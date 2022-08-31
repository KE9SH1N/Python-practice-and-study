#The key function for working with files in Python is the open() function.

#The open() function takes two parameters
#filename, and mode.

#There are four different methods(modes) for opening a file:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

#In addition you can specify if the file should be handled as binary or text mode

#"t" - Text - Default value. Text mode

#"b" - Binary - Binary mode(e.g. images)

#create a file


#open a file

import os



f = open("demofile.txt")


#read from file

f = open("demofile.txt", "r")
print(f.read())


#Open a file on a different location

f = open("D:\Programming\Python\python file handling\demofile.txt", "r")
print(f.read())


#read only a part of the file

f = open("D:\Programming\Python\python file handling\demofile.txt", "r")
print(f.read(5))


#readline() method
f = open("D:\Programming\Python\python file handling\demofile.txt", "r")
print(f.readline())


#loop in file

f = open("demofile.txt", "r")
for x in f:
  print(x)


#close file

f = open("demofile.txt", "r")
print(f.readline())
f.close()



#create and write on a file

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


#Delete a File
#To delete a file, you must import the OS module, and run its os.remove() function

os.remove("demofile.txt")


if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


#Remove the folder "myfolder"


os.rmdir("python file handling")
