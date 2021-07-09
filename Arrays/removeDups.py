def removeDuplicates(arr):
    if len(arr) < 1:
        return 0

    k = 0

    for i in range(len(arr)):
        if arr[i] != arr[k]:
            k += 1
            arr[k] = arr[i]

    return k + 1