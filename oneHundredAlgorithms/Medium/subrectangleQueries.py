"""
Given a class which takes a 2D array (size m x n) of a rectangle create two methods:
- updateSubrectangle which takes coordinates and a newvalue and updates the values within 
    these coordinates to the new value
- getValue which returns the value at a certain coordinate
"""

rectangle = [[1, 2, 3, 4], 
            [5, 6, 7, 8], 
            [9, 0, 1, 2]]

class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue
                
    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


obj = SubrectangleQueries(rectangle)
res1 = obj.getValue(0, 0)
print(res1)
obj.updateSubrectangle(0, 0, 1, 2, 99)
res2 = obj.getValue(0, 0)
res3 = obj.getValue(1, 1)
print(res2)
print(res3)