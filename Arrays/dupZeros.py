def duplicateZeros(arr):
    dups = 0
    length = len(arr) - 1

    for i in range(length + 1):
        if i > length - dups:
            break
        if arr[i] == 0:
            if i == length - dups:
                arr[length] = 0
                length -= 1
                break
            dups += 1

    last = length - dups

    for j in range(last, -1, -1):
        if arr[j] == 0:
            arr[j + dups] = 0
            dups -= 1
            arr[j + dups] = 0
        else:
            arr[j + dups] = arr[j]
    return arr


print(duplicateZeros([2, 0, 3, 4, 0, 3, 0]))
