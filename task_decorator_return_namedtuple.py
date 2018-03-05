from collections import namedtuple


def return_namedtuple(*x):  # принимаем аргументы декоратора
    def decorator(func):  # тут у нас функция
        def wrapper(*args, **kwargs):  # обертка с аргументами функции
            a = func(*args, **kwargs)  # задаем а
            if isinstance(a, tuple):  # если это кортеж
                new_tuple = namedtuple('my_tuple', list(x))  # делаем именованный кортеж с аргументами из самого верха
                a = new_tuple(*a)  # добавляем эл-ты в кортеж
                return a
            else:
                return a  # а если это не кортеж, то просто возвращаем а
        return wrapper
    return decorator

"""
@return_namedtuple('one', 'two', 'three')
def func():
    return 1, 2, 3

r = func()
print(r.three) # 3
"""
# крайне бесячее задание -_-; я это сделал, но зачем??????
