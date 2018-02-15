def fibonacci(n):
    f0 = 0
    f1 = 1
    f = []
    for i in range(n):
        f0, f1 = f1, f0 + f1
        f.append(f0)
        yield f
