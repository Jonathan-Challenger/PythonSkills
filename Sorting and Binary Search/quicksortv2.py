class QuickSort:
    def __init__(self):
        pass

    def quicksort(self, arr, left, right):
        if left < right:
            pos = self.partition(arr, left, right)
            self.quicksort(arr, left, pos - 1)
            self.quicksort(arr, pos + 1, right)

    def partition(self, arr, left, right):
        i = left
        j = right - 1
        pivot = arr[right]

        while i < j:
            while i < right and arr[i] < pivot:
                i += 1
            while j > left and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]

        return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]

print("Array before sorting: \n" + str(arr))
qs = QuickSort()
qs.quicksort(arr, 0, len(arr) - 1)
print("Array after sorting: \n" + str(arr))


