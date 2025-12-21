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
