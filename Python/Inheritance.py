class Vehicle:
    def __init__(self, vehicleType, noOfWheels, noOfDoors, noOfSeats):
        self.vehicleType = vehicleType
        self.noOfWheels = noOfWheels
        self.noOfDoors = noOfDoors
        self.noOfSeats = noOfSeats

    def get_info(self):
        print(self.vehicleType, self.noOfWheels, self.noOfDoors, self.noOfSeats)


if __name__ == '__main__':
    car = Vehicle('car', 4, 4, 5)
    car.get_info()
