import time


def pause(sec):
    def decorator(fuck):
        def wrapper(*args, **kwargs):
            time.sleep(sec)
            return fuck(*args, **kwargs)
        return wrapper
    return decorator


"""
@pause(5)
def fff():
    print('функция выполняется')
    return

fff()
выполняется дольше, чем через 5 секунд
"""