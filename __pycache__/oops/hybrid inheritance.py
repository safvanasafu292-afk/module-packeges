class Grandfather:
    def grand_father_features(self):
        print("Grandfather:wise & experienced")
class Father(Grandfather):
    def father_features(self):
        print("father:handling & caring")
class anut(Grandfather):
    def aunt_features(self):
        print("anut:kind& suppotive")
class child (Father ,anut):
    def aunt_features(self):
        print("child:english & curious")
c=child()
c.grand_father_features()
c.father_features()
c. aunt_features()
c. aunt_features()