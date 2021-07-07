nums = [2, 3, 3, 4, 5, 2, 3, 9]

def removeDuplicates(arr):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1


print(removeDuplicates(nums))