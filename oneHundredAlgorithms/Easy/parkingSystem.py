"""
Given a class of a parking system figure out if there is enough space for a new car to park.
There are three sizes of vehicle: big, medium and small. The input is an array of available
spaces in the car park (ex. [2, 0, 4]) and then cars can be added with addCar with the size that 
they are (ex. 1, 2, 3 is big, medium, small respectively). Return a boolean depending on if 
there is space in the car park for the new addCar.
"""



class parking():
    def __init__(self, big, medium, small):
        self.array = [big, medium, small]

    def addCar(self, carType: int):
        self.array[carType - 1] -= 1
        return self.array[carType - 1] >= 0
