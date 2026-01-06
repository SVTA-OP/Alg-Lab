def partition1(a, low, high):
    pivot = a[high]
    i = low
    j = high - 1
    while i < j:
        print(a)
        if a[i]  > pivot:
            while a[j] > pivot and i<j:
                j -= 1
            a[i],a[j] = a[j], a[i]
            # i += 1
            j -= 1
        else:
            i +=1
    a[i], a[high] = a[high], a[i]
    print(a)
    return i


print(partition1([9, 1, 8, 2, 7], 0, 4))
