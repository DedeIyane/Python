#even and odd numbers
li = list(range(1, 25))
even_numbers = []
odd_numbers = []

for item in li:
    if item  % 2 == 0:
        even_numbers.append(item)
    else:
        odd_numbers.append(item)

print(odd_numbers)
print(even_numbers)

#print the right triangle number pattern
rows = 5

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i, end=' ')
    print('')

#multiplication table pattern
num = 5

for i in range(1, num+1):
    for j in range(1, i+1):
        square= i*j
        print(square, end=' ')
    print('')

#full pyramid stars
stars= 6
for i in range(1, stars+1):
    for space in range(1, stars- i + 1):
        print(end=' ')
    for star in range(1, i+1):
        print('*', end=' ')
    print('')

#Right pyramid of stars
rstars= 5

for i in range(1, rstars+1):
    for j in range(1, i+1):
        print('*',end=' ')
    print('')

for k in range(rstars-1, 0, -1):
    for l in range(1, k+1):
        print('*', end=' ')
    print('')

#left pyramid of stars
lstars= 5

for i in range(1, lstars+1):
    for space in range(1, lstars-i+1):
        print(end=' ')
    for stars in range(1, i+1):
        print('*',end='')
    print('')
for j in range(lstars-1, 0, -1):
    for rspace in range(1, lstars-j+1):
        print(end=' ')
    for rstar in range(1, j+1):
        print('*', end='')
    print('')

#sandglass pattern
sglass= 5

for j in range(sglass, 0, -1):
    for gspace in range(1, sglass-j+1):
        print(end=' ')
    for gstar in range(1, j+1):
        print('*', end=' ')
    print('')

for i in range(1, sglass+1):
    for space in range(1, sglass-i+1):
        print(end=' ')
    for stars in range(1, i+1):
        print('*',end=' ')
    print('')

#pascal's triangle
from math import factorial
prows= 5

for n in range(prows):
    for space in range(1, prows-n):
        print(end=' ')
    
    for r in range(n+1):
        ncr= factorial(n) // (factorial(r) * factorial(n-r))
        print(ncr, end=' ')

    print('')

#Armstrong number
num= int(input('Enter a 3-digit number: '))

usum= 0

temp = num
while temp> 0:
    digit = temp% 10
    usum += digit ** 3
    temp//= 10

if num == usum:
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')

#armstrong numbers below 1000
snum= 1000

for num in range(1, snum):
    str_snum= str(num)
    num_powers= sum(int(digits) ** len(str_snum) for digits in str_snum)
    if num_powers == num:
        print(num, end=' ')
 

#fibonacci sequence
terms = int(input('Enter the number of terms: '))

n1, n2 = 0, 1

if terms <= 0:
    print(' Please enter a positive integer')

elif terms == 1:
    print(f'Fibonacci sequence: {n1}')

else:
    for term in range(terms):
        print(n1, end=' ')
        n= n1+n2
        n1 = n2
        n2 = n

#prime number
prime= int(input('Enter an integer'))

if num <= 1:
    print(f'{prime} is not a prime.')

elif prime > 1:
    for i in range(2, prime):
        if prime % i == 0:
            print(f'{prime} is not a prime.')
            print(f'{i} is a factor of {prime}.')
            break
    else:
        print(f'{prime} is a prime number.')

#Guessing game
import random

num= random.randint(1, 10)
guess= int(input('Enter a number between 1 and 10: '))

while guess != num:
    if guess < num:
        print('Your guess is too low.')
    elif guess > num:
        print('Your guess is too high.')

    guess= int(input('Guess again: '))
print('You guesses it right.')

#Counting digit, letter and special characters
sample = input('Enter a string: ')

d, l, o = 0, 0, 0

for c in sample:
    if c.isdigit():
        d += 1

    elif c.isalpha():
        l += 1

    else:
        o += 1

print(f' Digits: {d}')
print(f'Letters: {l}')
print(f'Other Characters: {o}')

#password validation
import re

pwd = input('Enter the password')
pwd_len= len(pwd)
is_valid= False

while True:
    if pwd_len < 7 or pwd_len > 20: break #if length of string is less than 7 and more than 20; return true and break the loop

    elif not re.search('[A-Z]', pwd): break #if no capital alphabet; return true and break the loop 

    elif not re.search('[a-z]', pwd): break #if no lowercase alphabet; return true and break the loop

    elif not re.search('[0-9]', pwd): break #if no integers; return true and break the loop
    
    elif not re.search('[$#@!]', pwd): break #if no special characters; return true and break the loop
    
    elif re.search('\s', pwd):break #if whitespaces are present; return true and break the loop

    else:
        is_valid = True
        break

if is_valid:
    print('Password is valid.')
else:
    print('Password is invalid.')

#palindrome
pal = input('Enter the string: ')
pal= pal.replace(' ', '').lower()
start= 0
end = len(pal) - 1
flag = True

while start < end:
    if pal[start] != pal[end]:
        flag = False
    start +=1
    end -=1

if flag:
    print(f'{pal} is a palindrome.')
else:
    print(f'{pal} is not a palindrome.')

#finding the HCF of two numbers using for loops
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        hcf = i

print(f'The HCF is {hcf}.')

#HCF of two numbers using Eucledian algorithm
num3 = int(input('Enter the first number: '))
num4 = int(input('Enter the second number: '))

if num3 < num4:
    num3, num4 = num4, num3

while num4 != 0:
    num1, num2 = num2, num1 % num2
print(f'The HCF is {num1}.')
