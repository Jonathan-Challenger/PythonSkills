"""
Given an m x n 2D array accounts where accounts[i][j] is the amount of money
the ith customer has in jth bank return the amount of money the richest customer
has
"""

test = [[1, 8], [4, 4, 3], [10], [3, 5, 8]]

def richestCustomer(accounts):
    for i in range(len(accounts)):
        accounts[i] = sum(accounts[i])
    return max(accounts)

print(richestCustomer(test))