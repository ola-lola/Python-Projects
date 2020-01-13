import sys

# 1

def hello_world():
    return "Hello world!"


# 2

def hello(name):
    if name == "" or None:
        return "Hello world!"
    else:
        return "Hello" + name


# 3

def print_hello(name):
    h = hello(name)
    print(h)


# 4

name = sys.argv[1]
print(hello(name))


#5

name = " ".join(sys.argv[1:])
print(hello(name))