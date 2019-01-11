'''
Created on Dec 27, 2018

@author: shishir.sarkar
'''
print('Hello Shishir welcome to python developement')

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

print('List examples')
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

print("-----------------------------Tuples Exaples--------------------")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

print("-----------------------------Dictionary--------------------------")
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

print("-----------------------------If else--------------------------")
a = 33
b = 34
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
x1 = 50;
x2 = 80;

if x1 == x2:
    print("x2 and x1 are equal..")
else:
    print("Nope you are wrong..")
     
print("Short Hand If ... Else")
print("A") if a > b else print("B")

print("One line if else statement, with 3 conditions:")
print("A") if a > b else print("=") if a == b else print("B")

c = 100
print("The and keyword is a logical operator,")
if a > b and c > a:
  print("Both conditions are True")      

print("The or keyword is a logical operator")
if a > b or a > c:
  print("At least one of the conditions are True")  