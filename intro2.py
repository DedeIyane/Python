num1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2= [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
items= [1, 2, 'N', 'Go', 3.14259]
print(num2[7])#to access elements in a list
print(items[-2])#negative indexing
#there can be a multidimensional list
my_list= [[1, 2, 3], 'Iyanu', [4, 5, 6]]
print(my_list[0][2])#to print 3
print(my_list[2])#to print entirety of 4, 5, 6

#adding elements to a list
languages= ['c', 'cpp', 'Java']
print(languages)
languages.append('python')#to add to the end of the list
languages.append('ruby')
languages.append('javascript')
print(languages)
languages.append(['R', 'C++'])#a list can be added to another list, making a single dimensional list multi
print(languages)

languages2= ['javascript', 'php', 'R']
print(languages2)
languages2.insert(0, 'Python')# list.insert(position, value), to add python to the start of the list
print(languages2)

more_langs= ['c++', 'C', 'Java', 'ruby']
print(more_langs)
languages2.extend(more_langs)#to add all items of a list in another list
print(languages2)

intro= 'I am Iyanu Dada'
print(intro.split())#to input a list using split method

#to change the an item in a list
num1[6]= 'Iyanu' #specifying the index to replace
print(num1)
items[2:4]= ['Bright', 'Iyanu', 'Dada']#to add multiple items
print(items)

#to remove list items
items.remove('Iyanu') #to remove item from a list
print(items)
items.pop(1) #to remove an item at a specified value, if value is not declared, it removes the last item
print(items)
del num1[2]
print(num1) #deletes an item at specified value, if value is specified, entire list is deleted
items.clear()#to empty the list but not delete it
print(items)

#list comprehension
names= ['John', 'James', 'Emmy', "Michael", "Jimmy"]
j_names=[]
for name in names:
    if 'J' in name:
        j_names.append(name)

print(j_names)
#or
i_names= [nam for nam in names if "J" in nam]
print(i_names)
names_copy= [nap for nap in names]
print(names_copy)

#DICTIONARIES
car= {'brand': 'Audi', 'model': 'A5'}
print(car['model'])
car['model']= 'A6' #valuses ate mutable
print(car['model'])

#to know the length of the dictionary, use the len() function
print(len(car))

#accessing dictionary items
print(car['brand'])#to access values using key names
print(car.get('model'))#to access values using get() method
print(car.keys())#to access keys of a dictionary
car['fuel type']= 'diesel'
print(car.keys())
print(car.values())#to access the values of a dictionary
print(car.items())#to access items in a dictionary

#Changing and adding dictionary items
car['model']= 'S5'#changing values using key names
print(car)
car.update({'model': 'A10'})#changing values using update()
car.update({'color': 'Blue'})#adding new items with update()
print(car)
car['Tyre']= 'Racing'#adding new items using key names
print(car)

#Removing dictionary items
print(car.pop('model'))#removing an item using pop()
print(car)
print(car.popitem())#removes the last inserted item
print(car)
del car['fuel type']#removing an item using del
print(car)
del car #removing a dictionary using del
car2= {'brand': 'ferrari', 'model': 'laferrari'}
print(car2)
car2.clear()
print(car2)

#copying a dictionary
car3= {'brand': 'BMW', 'model': 'M5'}
car4= car3.copy()
print(car4)
car5= dict(car4)
car5['color']= 'green'
print(car5)

#introduction to tuples
cars= ('Audi', 'Mercedes', 'BMW', 'Ferrari', 'Audi', 'Audi', 'BMW')
print(len(cars))#to determine the length of the tuple
car_color= tuple(('Blue', 'Green', 'Black', 'Blue', 'Red', 'Black', 'Red'))
print(car_color)
#to access tuple items
print(cars[1])#index can be used
print(car_color[-2])#negative indexing
print(car_color[1:4])#through splicing
print(cars[:])#to access whole tuple

#updating a tuple
#to add to a tuple, first convert it to a list
temp= list(cars)
temp.append('Toyota')
print(temp)
cars=tuple(temp)
print(cars)

#unpacking tuples
cars1, cars2, *cars3= cars
print(cars3)

print(num1[2] +num1[4])