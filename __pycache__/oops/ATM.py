#with abstractmethod
from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
class MyBankAtm(ATM):
    def withdraw(self):
        self.__verify_pin()
        self.__check_balance()
        self.__update_server()
        print("cash withdraw successfully")
    def __verify_pin(self):
        print("PIN verified")
    def __check_balance(self):
        print("balance checked")
    def __update_server(self):
        print("Server updated")
atm = MyBankAtm()
atm.withdraw()
#without abstraction

class MyBankAtm(ATM):
    def withdraw(self):
        print("cash withdraw successfully")

    def verify_pin(self):
        print("PIN verified")

    def check_balance(self):
        print("balance checked")

    def update_server(self):
        print("Server updated")

atm = MyBankAtm()
atm.verify_pin()
atm.check_balance()
atm.update_server()
atm.withdraw()
