class person:
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(self.name,"is walking")
class student(person):
    def study(self):
        print(self.name,"is studying")
s=student("anu")
s.study()
s.walk()
    