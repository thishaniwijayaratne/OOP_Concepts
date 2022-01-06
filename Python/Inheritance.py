class Vehicle(object):
    def __init__(self, vehicle_type, no_of_wheels, no_of_doors, no_of_seats):
        self.vehicle_type = vehicle_type
        self.no_of_wheels = no_of_wheels
        self.no_of_doors = no_of_doors
        self.no_of_seats = no_of_seats

    def get_info(self):
        print("This is a", self.vehicle_type, ".\nIt has", self.no_of_wheels, "wheels.",
              "\nIt has", self.no_of_doors, "doors,", "and", self.no_of_seats, "seats.\n\n")

    def is_car(self):
        if self.vehicle_type == "car" or self.vehicle_type == "Car":
            return True
        return False


class Car(Vehicle):
    def __init__(self, brand, no_of_wheels, no_of_doors, no_of_seats):
        self.brand = brand
        self.no_of_wheels = no_of_wheels
        self.no_of_doors = no_of_doors
        self.no_of_seats = no_of_seats
        self.price = 0
        self.vehicle_type = 'Car'

    def get_price(self):
        self.price = car_brand_prices[self.brand]* (self.no_of_wheels*250+self.no_of_doors*150+self.no_of_seats*200)
        print("Price of this ", type(self).__name__, "is", self.price)
        return self.price

    def is_car(self):
        return True


class MotorBike(Vehicle):
    def __init__(self, brand):
        self.brand = brand
        self.no_of_wheels = 2
        self.no_of_doors = 0
        self.no_of_seats = 2
        self.price = 0
        self.vehicle_type = 'Motor Cycle'

    def get_price(self):
        self.price = car_brand_prices[self.brand]* 100
        print("Price of this ", type(self).__name__, "is", self.price)
        return self.price


if __name__ == '__main__':
    global car_brand_prices
    car_brand_prices = {"Ferrari":25, "BMW": 20, "rolls royce":35}
    Lorry = Vehicle('Lorry', 6, 2, 3)
    Lorry.get_info()

    Car1 = Car("BMW", 4, 4, 6)
    Car1.get_info()
    Car1_cost = Car1.get_price()
