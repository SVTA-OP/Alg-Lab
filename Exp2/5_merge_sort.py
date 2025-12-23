def ordered_insert(u, v):
    if v == []:
        return [u]
    if u <= v[0]:
        return [u] + v

    return [v[0]] + ordered_insert(u, v[1:])

def ordered_merge(u,v):
    if u == []:
        # print(v)
        return v
    else:
        temp = u[0]
        v = ordered_insert(temp, v)
        return ordered_merge(u[1::], v)

def merge_sort(x):
    if len(x) <= 1:
        return x
    mid = len(x) // 2
    u = merge_sort(x[:mid])
    v = merge_sort(x[mid::])
    return ordered_merge(u,v)

a = [421,34,213,4325,243,3245,213]
print(merge_sort(a))
