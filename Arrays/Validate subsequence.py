array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence(arr1, seq):
    arrInd = 0
    seqInd = 0
    while arrInd < len(arr1) and seqInd < len(seq):
        if arr1[arrInd] == seq[seqInd]:
            seqInd += 1
        arrInd += 1
    return seqInd == len(seq)


print(isValidSubsequence(array, sequence))
