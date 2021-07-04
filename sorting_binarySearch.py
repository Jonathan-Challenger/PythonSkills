arr = [0, 7, 6, 4, 9, 3, 7, 3, 2, 5, 1, 9, 2]


# INSERTION SORT

def insertion_sort(seq):
    for i in range(1, len(seq)):
        to_sort = seq[i]

        while seq[i - 1] > to_sort and i > 0:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1

    return seq


print(insertion_sort(arr))

# QUICK SORT (O(nlog(n))
arr = [0, 7, 6, 4, 9, 3, 7, 3, 2, 5, 1, 9, 2]


def quick_sort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop()

    greater = []
    lower = []

    for item in seq:
        if item >= pivot:
            greater.append(item)
        else:
            lower.append(item)

    return quick_sort(lower) + [pivot] + quick_sort(greater)


print(quick_sort(arr))

# BUBBLE SORT
arr = [0, 7, 6, 4, 9, 3, 7, 3, 2, 5, 1, 9, 2]


def bubble_sort(seq):
    length = len(seq) - 1

    solved = False

    while not solved:
        solved = True
        for i in range(0, length):
            if seq[i] > seq[i + 1]:
                solved = False
                seq[i], seq[i + 1] = seq[i + 1], seq[i]

    return seq


print(bubble_sort(arr))

# SELECTION SORT
arr = [0, 7, 6, 4, 9, 3, 7, 3, 2, 5, 1, 9, 2]

def selection_sort(seq):
    length = range(0, len(seq) - 1)

    for i in length:
        mini = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[mini]:
                mini = j
        if mini != i:
            seq[mini], seq[i] = seq[i], seq[mini]

    return seq

print(selection_sort(arr))

# BINARY SEARCH OF SORTED LIST
arr = [0, 7, 6, 4, 9, 3, 7, 3, 2, 5, 1, 9, 2]
sortedd = quick_sort(arr)

def binary_search(seq, target):
    start_ind = 0
    end_ind = len(seq) - 1

    while start_ind <= end_ind:
        midpoint = start_ind + (end_ind - start_ind) // 2
        midpoint_val = seq[midpoint]

        if midpoint_val == target:
            return midpoint
        elif target < midpoint_val:
            end_ind = midpoint - 1
        else:
            start_ind = midpoint + 1

    return None

print(binary_search(sortedd, 5))


