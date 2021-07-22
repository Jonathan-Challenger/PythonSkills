"""
Given a string of a number n return the miniumum number of deci-binary (digits are only 0 or 1)
numbers needed to sum up to n
"""

test = '5467'

"""
5 4 6 7 
1 1 1 1
1 1 1 1 
1 1 1 1 
1 1 1 1
1 0 1 1
0 0 1 1
0 0 0 1

The sum of all the rows will equal the target number so the number of rows is the minimum number
of deci-binary numbers needed to sum to n. 
The number of rows is always the biggest digit in n. 
So to solve we simply find the biggest digits in n.
"""
def minPartitions(n):
    return int(max(n))

print(minPartitions(test))