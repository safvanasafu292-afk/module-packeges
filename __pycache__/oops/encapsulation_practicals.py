#Create a class with public, protected, and private variables and print each one.
class Demo:
    def __init__(self):
        self.public_var = "I AM PUBLIC"
        self._protected_var = "I AM PROTECTED"
        self.__private_var = "I AM PRIVATE"
    def show(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)
    def get_private(self):
        return self.__private_var
obj=Demo()
print(obj.public_var)
print(obj._protected_var)
print(obj.get_private())
#Write a class Student where _marks is private. Add methods to set and get marks safely.
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.grade = "A"

    def get_mark(self):
        return self.mark
student1 = Student("safu", 90)
print(student1.name)
print(student1.grade)
print(student1.get_mark())
#Create a BankAccount class with a private balance and methods to deposit and withdraw.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())
#Make a class Car with a protected variable _speed and a method to increase speed. Access _speed from a child class.
class Car:
    def __init__(self):
        self._speed = 0

    def increase_speed(self):
        self._speed += 10

class SportsCar(Car):
    def show_speed(self):
        print("Speed:", self._speed)

car = SportsCar()
car.increase_speed()
car.increase_speed()
car.show_speed()
#Demonstrate that private variables cannot be accessed directly but can be accessed using name-mangling.
class Student:
    def __init__(self):
        self.__mark = 90
student = Student()
print(student._Student__mark)
#Create a class with a private method __show_secret() and call it from another public method.
class Secret:
    def __show_secret(self):
        print("This is a secret")
    def show(self):
        self.__show_secret()
obj = Secret()
obj.show()
#Build a User class where password is private and only accessible through a check_password() method.
class User:
    def __init__(self, password):
        self.__password = password
    def check_password(self, password):
        return self.__password == password
user = User("12345")
print(user.check_password("12345"))
print(user.check_password("99999"))
#Make a class where a protected method _calculate_bonus() is inherited and used by a subclass.
class Employee:
    def _calculate_bonus(self, salary):
        return salary * 0.10
class Manager(Employee):
    def show_bonus(self):
        bonus = self._calculate_bonus(50000)
        print("Bonus:", bonus)
manager = Manager()
manager.show_bonus()
#Create a class that hides a private variable but updates it using setter and getter methods.
class Student:
    def __init__(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        if mark >= 0 and mark <= 100:
            self.__mark = mark
        else:
            print("Invalid mark")

student = Student(80)
print(student.get_mark())
student.set_mark(90)
print(student.get_mark())
#Write a real-world example (like ATM, Employee Salary, Game Player Stats) using encapsulation with private data.
class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Wrong PIN")

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Wrong PIN")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful")


atm = ATM(5000, 1234)

atm.check_balance(1234)
atm.deposit(1000)
atm.withdraw(2000, 1234)
atm.check_balance(1234)
