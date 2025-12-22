def print_array(a, low, high):
    while low <= high:
        print(a[low], end=" ")
        low += 1
    print()


def read_array():
    s = input("Enter elements: ")
    count = 0
    l = []
    for i in s:
        count += 1
        l.append(int(i))
    print("Number of elements:", count)
    return l


def minimum(a):
    n = 0
    while True:
        if a[n] == a[-1]:
            break
        n += 1
    n += 1
    min_index = 0
    for i in range(n):
        if a[i] < a[min_index]:
            min_index = i
    return min_index


def minimum2(a, low, high):
    min_index = low
    for i in range(low + 1, high + 1):
        if a[i] < a[min_index]:
            min_index = i
    return min_index


def minimum3(a, low, high):
    if low == high:
        return low
    else:
        min_rest = minimum3(a, low, high - 1)
        if a[high] < a[min_rest]:
            return high
        else:
            return min_rest


def selection_sort_q7(a):
    n = len(a)
    for i in range(n):
        min_idx = minimum2(a, i, n - 1)
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def selection_sort_q8(a, start, n):
    if start >= n - 1:
        return
    min_idx = minimum3(a, start, n - 1)
    a[start], a[min_idx] = a[min_idx], a[start]
    selection_sort_q8(a, start + 1, n)


def SelectionSortq6(a, n):
    if n <= 1:
        return a
    min_idx = minimum2(a, 0, n - 1)
    a[0], a[min_idx] = a[min_idx], a[0]
    SelectionSortq6(a, n - 1)
    return a


print_array([5, 10, 15, 20, 25], 1, 3)
print(read_array())
print(minimum([20, 10, 15, 20, 25]))
print(minimum2([20, 10, 15, 20, 25], 1, 4))
print(minimum3([20, 10, 15, 20, 25], 1, 4))
a = [20, 10, 15, 5, 25]
selection_sort_q7(a)
print(a)
b = [20, 10, 15, 5, 25]
selection_sort_q8(b, 0, len(b))
print(b)
c = [20, 10, 15, 5, 25]
SelectionSortq6(c, len(c))
print(c)
