def merge(u,v):
    if v == []:
        # print("U: ",u)
        return u
    elif u == []:
        # print("V: ",v)
        return v
    if u[0] <= v[0]:
        return [u[0]] + merge(u[1:], v)
    elif u[0] > v[0]:
        return [v[0]] + merge(u, v[1:])

a = [2 ,3 ,8 ,9]
b = [1 ,4 ,5 ,7]

print(merge(a,b))
