class GrandParent():
    def feature_garndparent(self):
        print("GrandParent feature")

class parent(GrandParent):
    def  feature_parent(self):
        print("parent feture")
class child(parent):
    def feature_child(self):
        print("child feature")
c=child()
c.feature_garndparent()
c. feature_parent()
c.feature_child()
    