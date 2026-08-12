#Write an abstract class Vehicle with an abstract method start. Create Car and Bike classes that implement it.
from abc import ABC ,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car starts")
class bike(vehicle):
    def start(self):
        print("bike start")
car=car()
bike=bike()
car.start()
bike.start()  
#Create an abstract class Payment with a method pay. Implement it in CardPayment and UPIPayment.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CardPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Card")
class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")
card = CardPayment()
upi = UPIPayment()

card.pay(500)
upi.pay(300)
#Make an abstract class Device with a method boot). Hide internal steps like __load_os) and __check_hardware() inside boot().
from abc import ABC,abstractmethod
class device(ABC):
    @abstractmethod
    def boot(self):
        pass
class laptop(device):
    def boot(self):
        self.__load_os()
        self.__check_hardware()
        print("laptop open")
    def __load_os(self):
        print("system openinig")
    def __check_hardware(self):
        print("hardware checked")

laptop=laptop()
laptop.boot()
#Create a non-abstract version of the same program and compare readability.
class Device:

    def boot(self):
        self.load_os()
        self.check_hardware()
        print("Device started")

    def load_os(self):
        print("Operating system loaded")

    def check_hardware(self):
        print("Hardware checked")


device = Device()

device.load_os()
device.check_hardware()
device.boot()

#Create an abstract class Account with a method calculate_interest). Subclasses: SavingAccount,currentacount.
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def calculate_interest(self, amount):
        pass
class SavingAccount(Account):
    def calculate_interest(self, amount):
        interest = amount * 0.05
        print("Savings interest:", interest)
class CurrentAccount(Account):
    def calculate_interest(self, amount):
        interest = amount * 0.02
        print("Current account interest:", interest)
saving = SavingAccount()
current = CurrentAccount()
saving.calculate_interest(10000)
current.calculate_interest(10000)
#Create an abstract class LoginSystem with login(). Inside login, call private methods like _ verity_user) and __check_password).
from abc import ABC, abstractmethod

class LoginSystem(ABC):

    @abstractmethod
    def login(self):
        pass

class UserLogin(LoginSystem):

    def login(self):
        self.__verify_user()
        self.__check_password()
        print("Login successful")

    def __verify_user(self):
        print("User verified")

    def __check_password(self):
        print("Password checked")

user = UserLogin()
user.login()
#Build a simple CoffeeMachine class where internal steps (grind beans, heat water, brew) are hidden inside make_coffee().
class CoffeeMachine:
    def make_coffee(self):
        self.__grind_beans()
        self.__heat_water()
        self.__brew()
        print("Coffee is ready")

    def __grind_beans(self):
        print("Beans are ground")

    def __heat_water(self):
        print("Water is heated")

    def __brew(self):
        print("Coffee is brewed")


machine = CoffeeMachine()
machine.make_coffee()
#Create a Shape class with an abstract method area() and implement it in Square, Circle, Triangle.
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
square = Square(5)
circle = Circle(3)
triangle = Triangle(4, 6)

print("Square:", square.area())
print("Circle:", circle.area())
print("Triangle:", triangle.area())
#Make a ReportGenerator abstract class with a method generate(), hiding internal steps inside the method.
from abc import ABC, abstractmethod
class ReportGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass
class SalesReport(ReportGenerator):
    def generate(self):
        self.__collect_data()
        self.__process_data()
        self.__create_report()
        print("Report generated")

    def __collect_data(self):
        print("Data collected")

    def __process_data(self):
        print("Data processed")

    def __create_report(self):
        print("Report created")
\
report = SalesReport()
report.generate()
#Create a small example where forgetting abstraction causes errors due to calling functions in the wrong order.

class CoffeeMachine:

    def grind(self):
        print("Beans ground")

    def heat(self):
        print("Water heated")

    def brew(self):
        print("Coffee brewed")


machine = CoffeeMachine()


machine.brew()
machine.grind()
machine.heat()