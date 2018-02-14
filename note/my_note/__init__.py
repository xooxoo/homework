import sys
from my_note import storage

# Вместо красивого status'a пока 0 и 1
# Всегда выводится меню после проведенной операции
# Это все сделано на коленке и некрасиво :( Зато я понял, как это все работает ^^
get_connection = lambda: storage.connect('note.sqlite')  # лямбда-функция для установки соединения с БД


def action_show():
    """Показывает список всех задач"""
    with get_connection() as conn:
        cursor = storage.show_all(conn)
    for i in cursor:  # для каждого i в кортеже принтим значения заголовков //как сделать нормальное выравнивание?//
        print('{[title]} | {[status]} | {[created]}'.format(i, i, i))


def action_add():
    """Добавляет задачу в список задач"""
    task = input('\nНовая задача: ')
    with get_connection() as conn:
        title = storage.add_task(conn, task)
        return title


def action_edit():
    """Изменяет задачу"""
    with get_connection() as conn:
        show = storage.show_all(conn)
        for i in show:
            print('{[id]} | {[title]}'.format(i, i))
        key = input('Введите id ')
        title = input('Введите измененное название: ')
        chan = storage.edit(conn, key, title)
    return chan


def action_finish():
    """Завершает задачу"""
    with get_connection() as conn:
        show = storage.show_all(conn)  # это все классно было бы заменить, потому что повторяется
        for i in show:
            print('{[id]} | {[status]}'.format(i, i))
        key = input('Введите id для завершения задания ')
        chan = storage.finish(conn, key)
    return chan


def action_re():
    """Перезапускает начатую задачу"""
    with get_connection() as conn:
        show = storage.show_all(conn)  # это все классно было бы заменить, потому что повторяется
        for i in show:
            print('{[id]} | {[title]} | {[created]}'.format(i, i, i))
        key = input('Введите id для обнуления задачи: ')
        chan = storage.action_re(conn, key)
    return chan



def action_exit():
    """Выход"""
    sys.exit(0)


def main():
    """Делаем словарик и бесконечный цикл с вводом значений"""
    actions = {'1': action_show,
               '2': action_add,
               '3': action_edit,
               '4': action_finish,
               '5': action_re,
               '6': action_exit}
    with get_connection() as conn:  # инициализируем БД
        storage.init(conn)
    while 1:
        print(
            '1. Вывести список задач\n'
            '2. Добавить задачу\n'
            '3. Отредактировать задачу\n'
            '4. Завершить задачу\n'
            '5. Начать задачу заново\n'
            '6. Выход'
        )
        param = input("Введите команду: ")
        action = actions.get(param)
        if action:
            action()
        else:
            print('АШЫБКА!!!')
