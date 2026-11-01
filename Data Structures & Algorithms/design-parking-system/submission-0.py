class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.data = [big, medium, small] 

    def addCar(self, carType: int) -> bool:
        if self.data[carType - 1]:
            self.data[carType - 1] -= 1
            return True

        return False 
