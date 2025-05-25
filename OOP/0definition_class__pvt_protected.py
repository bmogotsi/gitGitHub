# https://www.pythoncheatsheet.org/cheatsheet/oop-basics
# 
# 
"""  
    Encapsulation
"""
# helps to protect the data and methods of an object from unauthorized access and modification.
# by using access modifiers
 


# Define a class named MyClass
class MyClass:

    # Constructor method that initializes the class object
    def __init__(self):

        # Define a protected variable with an initial value of 10
        # The variable name starts with a single underscore, which indicates protected access
        self._protected_var = 10

        # Define a private variable with an initial value of 20
        # The variable name starts with two underscores, which indicates private access
        self.__private_var = 20

# Create an object of MyClass class
obj = MyClass()

# Access the protected variable using the object name and print its value
# The protected variable can be accessed outside the class but
# it is intended to be used within the class or its subclasses
print(obj._protected_var)   # output: 10

# Try to access the private variable using the object name and print its value
# The private variable cannot be accessed outside the class, even by its subclasses
# This will raise an AttributeError because the variable is not accessible outside the class
print(obj.__private_var)    # AttributeError: 'MyClass' object has no attribute '__private_var'

"""
    Inheritance
"""
# Inheritance promotes 
#       code reuse 
#       and allows you to create a hierarchy of classes that share common attributes and methods

# Define a class named Animal
class Animal:

    # Constructor method that initializes the class object with a name attribute
    def __init__(self, name):
        self.name = name

    # Method that is defined in the Animal class but does not have a body
    # This method will be overridden in the subclasses of Animal
    def speak(self):
        print("")

# Define a subclass named Dog that inherits from the Animal class
class Dog(Animal):

    # Override the speak method of the Animal class
    def speak(self):
        print("Woof!")

# Define a subclass named Cat that inherits from the Animal class
class Cat(Animal):

    # Override the speak method of the Animal class
    def speak(self):
        print("Meow!")

# Create a Dog object with a name attribute "Rover"
dog = Dog("Rover")

# Create a Cat object with a name attribute "Whiskers"
cat = Cat("Whiskers")

# Call the speak method of the Dog class and print the output
# The speak method of the Dog class overrides the speak method of the Animal class
# Therefore, when we call the speak method of the Dog object, it will print "Woof!"
dog.speak()   # output: Woof!

# Call the speak method of the Cat class and print the output
# The speak method of the Cat class overrides the speak method of the Animal class
# Therefore, when we call the speak method of the Cat object, it will print "Meow!"
cat.speak()   # output: Meow!

"""
    Polymorphism
"""
# allows you to write code that can work with objects of different classes in a uniform way
#        is achieved by using method overriding or method overloading

# Method overriding 
#   is when a subclass provides its own implementation of a method that is already defined in its parent class.
# Method overloading 
#   is when multiple methods have the same name but different parameters. 
#       Python does not support method overloading directly, but it can be achieved using default arguments or variable-length arguments.

#The Shape class is defined with an abstract area method, which is intended to be overridden by subclasses.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    # The Rectangle class is defined with an __init__ method that initializes
    # width and height instance variables.
    # It also defines an area method that calculates and returns
    # the area of a rectangle using the width and height instance variables.
    def __init__(self, width, height):
        self.width = width  # Initialize width instance variable
        self.height = height  # Initialize height instance variable

    def area(self):
        return self.width * self.height  # Return area of rectangle


 # The Circle class is defined with an __init__ method
 # that initializes a radius instance variable.
 # It also defines an area method that calculates and
 # returns the area of a circle using the radius instance variable.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius instance variable

    def area(self):
        return 3.14 * self.radius ** 2  # Return area of circle using pi * r^2

# The shapes list is created with one Rectangle object and one Circle object. The for
# loop iterates over each object in the list and calls the area method of each object
# The output will be the area of the rectangle (20) and the area of the circle (153.86).
shapes = [Rectangle(4, 5), Circle(7)]  # Create a list of Shape objects
for shape in shapes:
    print(shape.area())  # Output the area of each Shape object


"""
    Abstraction
"""
#  it allows you to focus on the essential features of an object or system while ignoring the details that aren’t relevant to the current context 
#  abstraction is a powerful tool for managing complexity and improving code quality in object-oriented programming, 
#  and Python provides a range of options for achieving abstraction in your code.
#
#  achieved by using: 
#   abstract classes 
#   or interfaces.

#  abstract class
#       abstract class is a class that cannot be instantiated directly, but is meant to be subclassed by other classes.
# 
#  interfaces  
#       is a collection of method signatures that a class must implement in order to be considered “compatible” with the interface. .
#
#  Python does not have built-in support for abstract classes or interfaces, 
#  but they can be implemented using the abc (abstract base class) module.
# 


# Import the abc module to define abstract classes and methods
from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method for Rectangles
    def area(self):
        return self.width * self.height

# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self.radius ** 2

# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())