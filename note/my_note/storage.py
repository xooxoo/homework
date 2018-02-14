import os.path as pp
import sqlite3


def dict_factory(cursor, row):  # получаем мету из запроса
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    """Устанавливает соединение с БД"""
    if db_name is None:  # если базы нет, то мы создаем ее где-то в памяти?
        db_name = 'note.sqlite'
    conn = sqlite3.connect(db_name)  # создаем объект соединения
    conn.row_factory = dict_factory
    return conn  # ну и функция возвращает объект соединения


def init(conn, creation_script=None):
    """Инициализирует структуру таблицы, которая прописана в схеме"""
    if creation_script is None:  # если скрипт не передали в функцию, то прописываем путь к нему
        creation_script = pp.join(pp.dirname(__file__), 'resourses', 'schema.sql')
        'соединяем пути .join из возвращенных в .dirname'
    with conn, open(creation_script) as f:
        conn.executescript(f.read())  # выполняем sql в файле schema


def add_task(conn, task):  # передаем объект соединения и задачу
    if not task:  # проверяем перем. task на значения /задание не может быть пустым/
        raise RuntimeError('Ну напиши хоть что-то')
    with conn:
        conn = conn.execute('INSERT INTO note (title) VALUES (?)', (task, ))
        '''создаем курсор, вставляем в столбец title значение task, делаем это через кортеж, чтобы быть классными 
        и избежать инъекций'''
    return conn


def show_all(conn):
    """Показать все задачи"""
    with conn:
        cursor = conn.execute('SELECT id, title, created, status FROM note')
        return cursor.fetchall()


def edit(conn, key, title):
    """Изменить задачу"""
    with conn:
        cursor = conn.execute('''UPDATE note 
                              SET title=?
                              WHERE id=?''', (title, key))
    return cursor.fetchone()


def finish(conn, key):
    """Меняет значение поля status = 1, что означает, что задача завершена"""
    with conn:
        cursor = conn.execute('''UPDATE note
                              SET status=1
                              WHERE id=?''', (key,))
    return cursor.fetchone()


def action_re(conn, key):
    """Изменяет время создания на текущее время"""
    with conn:
        cursor = conn.execute('''UPDATE note
                              SET created=CURRENT_TIMESTAMP
                              WHERE id=?''',(key,))
    return cursor.fetchone()