"""
This program takes an integer array as input with length n
and outputs an array of length 2n where the output array is
a concatenation of two of the input arrays
"""

test1 = [1, 2, 3, 4]
test2 = [78, 4, 2, 34, 1, 0]

# input is integer array nums 
def concatArray(nums):
    return nums + nums 

print("Test 1 output: ", concatArray(test1))
print("Test 2 output: ", concatArray(test2))
