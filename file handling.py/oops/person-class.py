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
