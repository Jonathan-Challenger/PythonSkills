nums = [1, 1, 2, 3, 4, 4, 4, 5, 6, 6]

def removeDuplicates(arr):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1


print(removeDuplicates(nums))