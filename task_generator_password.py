import random


def password_generator(n):
    while True:
        f = [str(random.randint(0, 9)) for i in range(n)]  # тест работает даже на список
        f = ''.join(f)  # это я просто для красоты прикрутил вообще не нужно
        yield f
