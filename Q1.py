def OrderedInsert(a, j):
    if j == 0 or a[j] >= a[j - 1]:
        return
    a[j], a[j - 1] = a[j - 1], a[j]
    OrderedInsert(a, j - 1)


def InsertionSort(a, j, n):
    if j == n:
        return
    OrderedInsert(a, j)
    InsertionSort(a, j + 1, n)


a = [64, 34, 25, 12, 22, 11, 90]
InsertionSort(a, 0, len(a))
print(a)
