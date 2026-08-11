# class dog:
#     def speak(self):
#         return "woof"
# class cat:
#     def speak(self):
#         return "meow"
# def animal_sound(animal):
#     print(animal.speak())

# d=dog()
# c=cat()
# animal_sound(d)
# animal_sound(c)
#polymorphism with inheritance. Area of circle,rectangle
class shape:
    def area(self):
        return 0
class circle(shape):
    def area(self):
        return 3.14 * 5 * 5
class rectangle(shape):
    def area(self):
        return 10 * 5
shapes=[circle(),rectangle()]
for s in shapes:
    print(s.area())

