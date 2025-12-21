def ordered_insert(u, v):
    if not v:   
        return [u]
    if u <= v[0]:   
        return [u] + v
     
    return [v[0]] + ordered_insert(u, v[1:])


v = [5, 10, 20, 35, 50]
u = 15
print(ordered_insert(u, v))


def insertion_sort(v):
    if not v:   
        return []
    return ordered_insert(v[0], insertion_sort(v[1:]))
