"""
Given array nums which consists of 2n elements in the form
[x1, x2, ... xn, y1, y2, ... yn] return an array in the form
[x1, y1, x2, y2, ... xn, yn]
"""

test_arr = [1, 5, 4, 3, 7, 9]
n = 3

def shuffleArray(nums, n):
    return [num for i in range(n) for num in (nums[i], nums[i+n])]



print(shuffleArray(test_arr, n))
