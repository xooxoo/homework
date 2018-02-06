start = True

# Переложить функции, оставить только import


def status():
    print('ur tasks: ')


def add():
    print('add')


def edit():
    k = True
    while k:
        print('edit')
        print('type "0" for return')
        k = int(input())


def the_end():
    print('task completed')


def new_start():
    print('from start')


# d = {1: status(), 2: add(), 3: edit(), 4: the_end(), 5: new_start()}


while start:
    print(
        '1. Вывести список задач\n'
        '2. Добавить задачу\n'
        '3. Отредактировать задачу\n'
        '4. Завершить задачу\n'
        '5. Начать задачу сначала\n'
        '6. Выход')
    a = int(input('Введите число: '))

# Поменять ифы на что-нибудь хорошее

    if a == 1:
        status()
    if a == 2:
        add()
    if a == 3:
        edit()
    if a == 4:
        the_end()
    if a == 5:
        new_start()
    if a == 6:
        start = False

