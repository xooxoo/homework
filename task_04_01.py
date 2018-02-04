with open('data.txt', 'r') as data:
    n = int(input())
    p = int(input())
    for i in data:
        data = i.split(' ')
    with open('out-1.txt', 'w') as out_1:
        for i in data:
            if int(i) % n == 0:
                out_1.write('{} '.format(str(i)))
    with open('out-2.txt', 'w') as out_2:
        for i in data:
            out_2.write('{} '.format(str(int(i) ** p)))