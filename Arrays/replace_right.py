def replace_right_elements(arr):
    n = len(arr)
    mx = arr[n - 1]

    for i in range(n - 2, -1, -1):
        arr[i], mx = mx, max(mx, arr[i])

    arr[n - 1] = -1
    
    return arr

arr1 = [1, 18, 6, 8, 2, 3, 5]

print(replace_right_elements(arr1))