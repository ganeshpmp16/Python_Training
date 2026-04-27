class Vehicle:
    def start_engine(self):
        print("Engine starts.")
        
class Car(Vehicle):
    def drive(self):
        print("Car is driving.")
# Example usage
my_car = Car()
my_car.start_engine()  # Inherited method from Vehicle
my_car.drive()         # Method defined in Car
