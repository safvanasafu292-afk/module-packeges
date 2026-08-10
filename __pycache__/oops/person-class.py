#class=blueprint
class person:
    #Constructor=runs when object is created    
    def __init__(self,name,age):
        self.name=name
        self.age=age
#method=function inside class
    def greet(self):
        print("hello",self.name)
#object=createdfrom class
p=person("alice",20)
p.greet()
class car:
    def __init__(self,barnd,model):
        self.barnd=barnd
        self.model=model
    def start(self):
        print(self.barnd,self.model, "is starting")
car1=car("luxus","c350")
car2=car("bmw","x5")
car1.start()
car2.start()
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
student1=student("safu",21)
student1.display()
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area:", self.length * self.width)
r1 = Rectangle(10, 5)
r1.area()