# Модуль перевода числа из одной системы счисления в другую


def bin2dec(number):
    number = list(''.join(str(number)))
    k = 1
    c = []
    for p in range(len(number)):
        f = int(int(number[p]) * (2 ** (len(number) - k)))
        c.append(f)
        k += 1
    return sum(c)


def oct2dec(number):
    number = list(''.join(str(number)))
    k = 1
    c = []
    for p in range(len(number)):
        f = int(int(number[p]) * (8 ** (len(number) - k)))
        c.append(f)
        k += 1
    return sum(c)


def hex2dec(number):
    number = list(''.join(str(number).lower()))
    rpc = {'f': 15, 'e': 14, 'd': 13, 'c': 12, 'b': 11, 'a': 10}
    k = 1
    b = []
    c = []
    for i in number:
        if i in rpc:
            i = str(i)
            i = i.replace(i, str(rpc[i]))
            b.append(i)
        else:
            b.append(i)
    for p in range(len(number)):
        f = int(int(b[p]) * (16 ** (len(b) - k)))
        c.append(f)
        k += 1
    return sum(c)


def dec2bin(number):
    s = str()
    while number > 1:
        c = number % 2
        number = number // 2
        s = s + ''.join(str(c))
    if number <= 1:
        s = s + ''.join(str(number))
    s = s[::-1]
    return str(s)


def dec2oct(number):
    s = str()
    while number > 7:
        c = number % 8
        number = number // 8
        s = s + ''.join(str(c))
    if number <= 7:
        s = s + ''.join(str(number))
    s = s[::-1]
    return str(s)


def dec2hex(number):
    s = str()
    rpc = {'f': 15, 'e': 14, 'd': 13, 'c': 12, 'b': 11, 'a': 10}
    while number > 15:
        c = str(number % 16)
        for i in rpc:
            c = c.replace(str(rpc[i]),str(i))
        s = s + ''.join(str(c))
        number = number // 16
    if number <= 15:
        for i in rpc:
            number = str(number)
            number = number.replace(str(rpc[i]),str(i))
        s = s + ''.join(str(number))
    s = s[::-1]
    return str(s)

