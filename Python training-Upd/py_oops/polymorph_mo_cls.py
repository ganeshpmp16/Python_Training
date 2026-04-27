# method overriding  in polymorphism 
class Bird:
    def show(self):
        print("Bird  flying to fetch food")

class Sparrow(Bird):
    def show(self):
        print("Sparrow is flying to fetch water")
class Eagle(Bird):
    def show(self):
        print("Eagle is sitting on the mountain to remove its old feathers   and grow new feathers           ")
b1 = Sparrow()
b2 = Eagle()
b1.show()
b2.show()


