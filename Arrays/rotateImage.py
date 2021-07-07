"""
Given a 2D nxn matrix that represents an image. Rotate the matrix
90 degrees clockwise.
"""


def rotate_image(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for x in range(n):
        for l in range(n // 2):
            arr[x][l], arr[x][n - 1 - l] = arr[x][n - 1 - l], arr[x][l]

    return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in arr])


arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print("Before rotation:")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in arr2]))
print("After rotation:")
print(rotate_image(arr2))
