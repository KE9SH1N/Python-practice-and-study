#slice string

x = 'hello world'

print(x[0:5])

#modify string
#upper case & lower case

print(x.upper())
print(x.lower())


#remove whitespace from starting or ending point

print(x.strip())

#replace with something

print(x.replace("w","d"))

#split string

print(x.split())


#string concatenation

a = 'hello'
b = 'world'

c = a+ " " +b
print("c = " +c)

#string format (string and int cant combine)

age =36

text = 'my name is mishel and i am {}'

print(text.format(age))

#if we face multiple variable then we can use index number

q = 3
item = 567
price = 49.99

myorder = 'i want to pay {2} dollars for {0} pieces of item {1}'

print(myorder.format(q,item,price))

#escape character so that we can use quote inside a string

tex = 'we are the so called \"vikings"\ from the north'
print(tex)

#length method
print(len(c))
#first charecter
print(c[0])

print(c)
print(c[2:5])

