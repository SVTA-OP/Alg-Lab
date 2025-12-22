def ordered_insert(u, v):
    if not v:
        return [u]
    if u <= v[0]:
        return [u] + v

    return [v[0]] + ordered_insert(u, v[1:])


def insertion_sort(v):
    if not v:
        return []
    return ordered_insert(v[0], insertion_sort(v[1:]))


def q3(x, n):
    if n <= 1:
        return x

    temp = x[n - 1]

    insert_idx = n - 1

    for i in range(n - 2, -1, -1):
        if x[i] > temp:
            x[i + 1] = x[i]
            insert_idx = i
        else:
            break

    x[insert_idx] = temp
    return x


def oinsert(a, j):
    temp = a[j]
    ind = j

    for i in range(j - 1, -1, -1):
        if a[i] > temp:
            a[i + 1] = a[i]
            ind = i
        else:
            break

    a[ind] = temp
    return a


def oinsert_q5(a, j):
    f = a[j]
    j -= 1

    while j >= 0 and a[j] > f:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = f
    return a


def InsertionSortq6(a, n):
    if n <= 1:
        return a

    InsertionSortq6(a, n - 1)
    oinsert(a, n - 1)

    return a


def InsertionSortq8(a, n):
    for i in range(1, n):
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    return a


def IterativeInsertion(a, n):
    for i in range(1, n):
        oinsert(a, i)

    return a


v = [5, 10, 20, 35, 50]
u = 15
print(ordered_insert(u, v))
print(insertion_sort([5, 10, 20, 35, 50]))

x = [12, 13, 15, 16, 14]
n = 0
while True:
    if x[n] != x[-1]:
        n += 1
    else:
        n = n + 1
        break
print(q3(x, n))
print(oinsert([12, 13, 15, 16, 14], n - 1))
print(oinsert_q5([12, 13, 15, 16, 14], n - 1))
print(InsertionSortq6([12, 13, 15, 16, 14], n))
print(IterativeInsertion([12, 13, 15, 16, 14], n))
print(InsertionSortq8([12, 13, 15, 16, 14], n))
