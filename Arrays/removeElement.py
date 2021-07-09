def removeElement(arr, val):
    if len(arr) < 1:
        return 0
    
    k = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]
            k += 1
    return k

print(removeElement([1, 2, 3, 4, 4, 4, 5], 4))