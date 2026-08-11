# Create two classes Car and Bike, both having a method start). Call the same method for both objects and observe the different outputs.
class Car:
    def start(self):
        print("Car starts with a key")

class Bike:
    def start(self):
        print("Bike starts with a button")

car = Car()
bike = Bike()

car.start()
bike.start()
#  Create a parent class Animal with a method sound(). Create two subclasses Lion and Elephant that override sound(). Print the sound of each animal using a loop.
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Lion(Animal):
    def sound(self):
        print("Lion roars")

class Elephant(Animal):
    def sound(self):
        print("Elephant trumpets")

animals = [Lion(), Elephant()]

for animal in animals:
    animal.sound()
#  Wotea function show_are(shape) that calls shape.area0. Create classes Square and Circle with their own area methods and test the function.
class Square:
    def area(self):
        return 25

class Circle:
    def area(self):
        return 50.24

def show_area(shape):
    print("Area:", shape.area())

square = Square()
circle = Circle()

show_area(square)
show_area(circle)
# - Create a class EnglishGreeting with a method greet) returning "Hello". Create a class SpanishGreeting returning "Hola". Write a function that accepts any greeting object and calls greet).
class EnglishGreeting:
    def greet(self):
        return "Hello"

class SpanishGreeting:
    def greet(self):
        return "Hola"

def show_greeting(greeting):
    print(greeting.greet())

english = EnglishGreeting()
spanish = SpanishGreeting()

show_greeting(english)
show_greeting(spanish)
#  Use the built-in function len with different data types- string, list, tuple- and identify how built-in polymorphism works.
name = "Python"
numbers = [10, 20, 30, 40]
values = (1, 2, 3)

print(len(name))
print(len(numbers))
print(len(values))
# - Create a class Laptop with a method price). Create two subclasses GamingLaptop and BusinessLaptop overriding price). Print prices using polymorphism.
class Laptop:
    def price(self):
        print("Laptop price: ₹50,000")

class GamingLaptop(Laptop):
    def price(self):
        print("Gaming Laptop price: ₹1,00,000")

class BusinessLaptop(Laptop):
    def price(self):
        print("Business Laptop price: ₹70,000")

laptops = [GamingLaptop(), BusinessLaptop()]

for laptop in laptops:
    laptop.price()
# - make classes Dog, Cat, and Cow with a speak method. Store objects in a list and call speak inside a loop.
class Dog:
    def speak(self):
        print("Dog says Woof")

class Cat:
    def speak(self):
        print("Cat says Meow")

class Cow:
    def speak(self):
        print("Cow says Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()
# - Create a class Shape with a method draw). Override it in subclasses Triangle and Circle. Demonstrate polymorphism by calling draw) on each.
class Shape:
    def draw(self):
        print("Drawing a shape")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

shapes = [Triangle(), Circle()]

for shape in shapes:
    shape.draw()
# - Write a function that receives any object with a show() method. Create two classes with different show) behaviors and use them with the function.
class Student:
    def show(self):
        print("Student details")

class Teacher:
    def show(self):
        print("Teacher details")

def display(obj):
    obj.show()

student = Student()
teacher = Teacher()

display(student)
display(teacher)
# - create classes PDFReader and ImageViewer, each having an open) method. Call open) for both objects and observe polymorphism.
class PDFReader:
    def open(self):
        print("Opening PDF file")

class ImageViewer:
    def open(self):
        print("Opening image file")

files = [PDFReader(), ImageViewer()]

for file in files:
    file.open()
