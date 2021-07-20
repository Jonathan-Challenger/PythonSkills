"""
This is a program that takes an array of integers as input and 
builds an array where ans[i] = nums[nums[i]]. This array of the same length 
is then returned.
"""

test1 = [0, 2 ,1, 6, 2, 5, 3]
test2 = [9, 3, 5, 1, 3, 2, 6, 6, 2, 5]

# nums is the only input and is an array of integers
def buildArray(nums):
    return [nums[nums[i]] for i in range(len(nums) - 1)]  # Simply builds array with the permutation using list comprehension

print("Test 1 output: ", buildArray(test1))
print("Test 2 output: ", buildArray(test2))


