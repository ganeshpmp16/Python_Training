# function working in different objects
class Bird:
    def move(self):
        print("Bird  flying to fetch food")
class Fish:
    def move(self):
        print("Fish is swimming to fetch water")
        
def show_move(obj):
    obj.move()

show_move(Bird())
show_move(Fish())
