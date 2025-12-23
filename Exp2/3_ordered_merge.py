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


a = [45]
b = [5,10,15,20,25,30,35,40,50]

print(ordered_merge(a, b))



        
