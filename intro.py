print("Hello World")
### Identations ###
name= 'Iyanu'

if name == 'Iyanu':
    print('Hello Iyanu')
    print('How are you?')
else:
    print('Hello there!\n')
    print('Who are you')

###Read Evaluate Print Loop###

REPL= (2**3, 3%2, 2//2, 2/2, 2*3, 8-2, 2+2)
print(REPL)

###Data Types###

integers= (-1, 2, 0, 50000)
floats= (175.256, 0.017, 1.3e3, 1.66e-3)
###Boolean data type represents any True or False###
strings= ('Hello world')

###Variables in python###
x= 50
y= 79
print(x+y)
studentName= 'Iyanu Dada'###camel case convention###
StudentName= 'Akinlolu Dada'###pascal case convention###
student_name= 'Bright Dada'###snake case convention###

###chained assignments###
a= b= c= 75
print(x+b)

###string data type###
statement1= "The language is 'python' and named after Monty Python."
statement2= 'Hello! \'I am Iyanu\'. How\'s ypur mother?.'
statement3= '''Hello world!:
This is Iyanu.
How are you?''' ###multi-line string###
print(statement3)

###Accessing   characters in a string###
print(student_name [0]) ####to print I###
print (student_name [-1]) ###from the last character to print a###
print(student_name [3:7]) ###to access substring of a string and print 'ght ' [start_index:end_index]###
print(student_name [:3]) ###start_index can be indicated as 0 or left blank to access###

### '+' to concatenate two strings together###
surname= 'Dada'
firstname= 'Iyanu'
print(firstname + surname)

### '*' can create multiple copies of a string###
first_3 = 3 * firstname
print(first_3)

###string comparison operators###
print('iyanu'== 'Iyanu') ### Equality operator###
print('iyanu'!= 'Iyanu') ### Not equal operator###
print('football' < 'Football') ### Less than###
print('football' <= 'football') ### Less than and equal to###
print('soccer' > 'Soccer') ### greater than###
print('soccer' >= 'Soccer') ### greater than and equal to###

### membership operators###
print('Iya' in 'Iyanu') ###returns true if the operand is contained within the second operand###
print('yIn' not in 'Iyanu')###returns true if the first operand is not contained within the second operands###

### string formating operator %d, %c, %s, %f
age= 22
print('My age is %d' %(age))

###string slicing###
fullname= 'I am Iyanu Dada'
s= fullname
print(s[0:10])
print(s[2:9])
print(s[0:10:2])#step value is -1 the indicated value so will print 'Ia yn'
l= 'abc'*4
print(l[::3])#aaaa will be printed
print(s[12:3:-3])###3+1 for the stop index, -3 +1 for the step value
print(s[::-1])#to reverse a string

#string formatting
fname= firstname
sname= surname
city= 'lagos'
age= 22
print('My name is %s %s and I live in %s. I am %d years old.' %(fname, sname, city, age))
print('I live in {2} and I\'m {3} years old. My name is {0} {1}.' .format(fname, sname, city, age))#indexing starts from zero
print(f'I am {fname} {sname}, I am {age} years old and I live in {city}')#f-string formatting
introduction= (f'My name is {fname} {sname}.'
               f'My age is {age} years old.'
               f'I live in {city}.')
print(introduction)
print(f'The value for x + y is {x + y}')

#string methods
sayhi= '     Hello World     '
print(sayhi.strip())###if empty, removes leading and trailing white spaces.
print(sayhi.lstrip())#to remove only leading whitespaces
print(sayhi.rstrip())#to remove trailing white spaces
intro= f'I am {fname} {sname}, I am {age} years old and I live in {city}'
print(intro.split(' ',8))# .split('separator', max split)
print(intro.rsplit(' ',8))
l1= ["H", 'e', 'l', 'l', 'o']
print(''.join(l1))#separator.join(iterable)
l2= ['I', 'am', 'not', 'your', 'boyfriend']
print(' '.join(l2))
print(intro.replace('am', 'am not', 1).replace(' ', '_')) #for replace, string.replace(old string, new string, count)
print(intro.upper())#does not support any argument, just capitalizes the whole string
print(sayhi.lower())# to convert all letters to lowercase
l_intro= intro.lower()
print(l_intro)
print(l_intro.capitalize())# to capitalize the first character
# .isupper() returns true if all characters are uppercase, .islower() returns true if all characters are lowercase
# .isalpha() returns true when all characters are alphabets, isnumeric() returns true if all characters are numbers
print(intro.isalpha()) #False because of whitespaces
# .isalnum() returns true if all characters are alphanumeric
print(intro.count('a'))#syntax is .count(substring, start index, end index)
print(intro.find('am'))#syntax is .find(sub, start, end), returns index of first occurence. 
print(intro.rfind('am'))#rfind() returns index of last occurence
#smae goes for .index() and .rindex()