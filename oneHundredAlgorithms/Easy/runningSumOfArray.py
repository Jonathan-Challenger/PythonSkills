"""
This program takes in an integer array nums as input and then computes
the running sum of all items in nums. An array of the running sum is then 
output
"""

test1 = [1, 2, 3, 4]
test2 = [78, 4, 2, 34, 1, 0]

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums

print("Test 1 output: ", runningSum(test1))
print("Test 2 output: ", runningSum(test2))