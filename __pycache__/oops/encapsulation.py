# class Demo:

#     def __init__(self):
#         self.public_var = "I AM PUBLIC"
#         self._protected_var = "I AM PROTECTED"
#         self.__private_var = "I AM PRIVATE"

#     def show(self):
#         print(self.public_var)
#         print(self._protected_var)
#         print(self.__private_var)
#     def get_private(self):
#         return self.__private_var
    
# obj = Demo()
# print(obj.public_var)
# print(obj._protected_var)
# print(obj.get_private())
# #student program
# class Student:

#     def __init__(self, name, mark):
#         self.name = name          # Public
#         self._grade = "A"         # Protected
#         self.__mark = mark        # Private

#     def get_mark(self):
#         return self.__mark


# student = Student("Safvana", 90)

# print(student.name)
# print(student._grade)
# print(student.get_mark())
# #employee
# class Employee:
#     def __init__(self):
#         self.name = "Anu"
#         self._department = "HR"
#         self.__salary = 50000

#     def get_salary(self):
#         return self.__salary

# emp = Employee()

# print(emp.name)
# print(emp._department)
# print(emp.get_salary())

# #bank balance
# class bankaccount:
#     def __init__(self):
#         self.owner="rahul"
#         self._branch="kpm"
#         self.__balance=90000
#     def get_balance(self):
#         return self.__balance
# act=bankaccount()
# print(act.owner)
# print(act._branch)
# print(act.get_balance()) 
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


acc = BankAccount(20000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())