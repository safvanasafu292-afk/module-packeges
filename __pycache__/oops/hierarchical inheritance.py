class vehicle:
    def start(self):
        print("vehicle starting")
class car(vehicle):
    pass
class bike(vehicle):
    pass
c=car()
c.start()
b=bike()
b.start()