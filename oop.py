#Encapsulation: Prefixing attributes and methods with a single underscore means they are meant for internal use. 
# This is a convention, and it doesn't enforce accessing attributes from the outside. 
# Prefixing attributes and methods with a double underscore effectively prevents them from being accessed from outside of their class.
class Wallet:
   def __init__(self, balance):
       self.__balance = balance # Private attribute

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount # Remove from the balance safely

account = Wallet(500)
print(account.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'

#Properties are used instead of methods for better readability and cleaner code. 
# They let you access values with dot notation, like regular attributes, without parentheses.
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get the radius
        return self._radius
  
    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)

#To create the setter that will set the radius, 
# you have to define another method with the same name and use @<property_name>.setter above it
    @radius.setter
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value
#When setting a value, you should not assign to the property name itself because that will cause a RecursionError. 
# Use a separate internal name, often with an underscore, to store the value.
  # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius
my_circle = Circle(3)

print(my_circle.radius) # 3
print(my_circle.area) # 28.26

print('Initial radius:', my_circle.radius) # Initial radius: 3

my_circle.radius = 8
print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8



#Inheritance
#Inheritance: The process by which a child class uses the attributes and methods of a parent class. 
# Inheritance promotes code reuse, provides clear hierarchies, and customizes behavior without rewriting everything. 
# To implement inheritance, a child class takes in the name of a parent class
class Parent:
    pass
    # Attributes and methods for Parent

class Child:
    pass
    # Attributes and methods for Child

class GrandChild(Parent, Child):
    pass
    # GrandChild inherits from both Parent and Child
    # GrandChild can combine or override behavior from each
#super() Function: A function that lets you call a method from a parent class, 
# when a class has a different implementation of that method, or it extends the method, without duplicating code.





#Polymorphism:The OOP principle that lets different classes use the same method name, 
# but each class implements it differently when called.
class A:
   def action(self):
       pass

class B:
   def action(self):
       pass

class C:
   def action(self):
       pass

#Class().method()   Works for A, B, or C

#Name Mangling: A process in which Python internally renames an attribute prefixed with a double underscore 
# by adding an underscore and the class name as a prefix, turning __attribute into _ClassName__attribute.
#The main purpose of name mangling is to prevent accidental attribute and method overriding when you use inheritance.
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}



#Abstraction: A programming concept in which complex implementation details of object or system are hidden and only the essential features are shown. 
# In Python and other programming languages, abstraction simplifies complex systems by increasing reusability.
from abc import ABC, abstractmethod

# Define an abstract base class
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Concrete subclass that implements the abstract method
class ConcreteClassOne(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassOne')

# Another concrete subclass
class ConcreteClassTwo(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassTwo')