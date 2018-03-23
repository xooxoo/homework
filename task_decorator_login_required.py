import hashlib


def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()


def login_required(func):
    def wrapper(*args, **kwargs):
        i = 3
        while i != 0:
            username = input()
            password = input()
            with open('token.txt') as f:
                check = f.read()
                token = make_token(username, password)
                if check == token:
                    return func(*args, **kwargs)
                i -= 1
        return func(*args, **kwargs)
    return wrapper








