arr = [1, 2, 3, 3, 4, 7, 5, 3, 1]

def mountain(arr):
    i = 0

    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        i += 1
    
    if i == 0 or i == len(arr) - 1:
        return False

    while i + 1 < len(arr) and arr[i] > arr[i + 1]:
        i += 1
    
    return i == len(arr) - 1

    


print(mountain(arr))


