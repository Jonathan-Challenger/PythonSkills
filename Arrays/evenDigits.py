def even_digits(arr):
    count = 0
    lens = []

    for i in range(len(arr)):
        lens.append(len(str(i)))
        for n in lens:
            if n % 2 == 0:
                count += 1
    return count

print(even_digits([12, 2, 565, 1233, 6767, 34, 2, 76778]))

