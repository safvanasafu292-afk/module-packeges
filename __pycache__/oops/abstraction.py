from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        return "woof"
class cat(animal):
    def sound(self):
        return "meow"
d=dog()
c=cat()
print(d.sound())
print(c.sound())

#payment system 
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(payment):
    def pay(self,amount):
        print("paid",amount,"using UPI")
class card(payment):
    def pay(self,amount):
        print("paid",amount,"usind card")


p1=UPI()
p2=card()
p1.pay(500)
p2.pay(100)
