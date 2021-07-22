"""
We are given an int array candies where candies[i] is the number of candies
for the ith child and an integer extra which is how many extra candies
I have to give away. Return a boolean array where the result is true 
if after giving the ith child extra candies they will have the greatest number
of candies
"""

candies = [4, 2, 6, 5, 8]
extra = 4

def mostCandies(candies, extra):
    most_candies = max(candies)
    for i in range(len(candies)):
        if candies[i] + extra >= most_candies:
            candies[i] = True
        else:
            candies[i] = False
    return candies

print(mostCandies(candies, extra))