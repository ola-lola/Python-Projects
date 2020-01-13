def hello_world():
    return "Hello world!"


def hello(name):
    if name == "" or None:
        return "Hello world!"
    else:
        return "Hello" + name


def print_hello(name):
    h = hello(name)
    print(h)

