class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")
d=dog()
d.eat()
d.bark()
