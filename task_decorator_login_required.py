import hashlib


def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()


def login_required():
