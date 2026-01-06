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

def QuickSort(a, low, high):
    if low < high:
    
        p = partition1(a,low,high)
        u = QuickSort(a, low, p-1)
        v = QuickSort(a, p+1, high)
        print(a)


print(QuickSort([7,5,8,2,3,6], 0,5))
