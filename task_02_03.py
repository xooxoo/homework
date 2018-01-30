def average(lst):
    k = 0
    for i in range(len(lst)):
        k = k + lst[i]
        if i == len(lst)-1:
            k = k/len(lst)
    return float(round(k,3))