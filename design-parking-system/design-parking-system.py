class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_space = {
            1: big,
            2: medium,
            3: small
        }
        

    def addCar(self, carType: int) -> bool:
        if self.parking_space[carType] > 0:
            self.parking_space[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)