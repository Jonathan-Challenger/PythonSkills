def even_digits(arr):
    lens = []
    count = 0
    for i in arr:
        l = len(str(i))
        lens.append(l)
    for n in lens:
        if n % 2 == 0:
            count += 1
    return count

print(even_digits([12, 2, 565, 1233, 6767, 34, 2, 76778]))

