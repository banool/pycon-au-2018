def my_decorator(func):
    def new_func():
        return func() + "!!!!"
    return new_func

@my_decorator
def hello_pycon():
    return "Hello Pycon AU 2018!"

print(hello_pycon())

hello_pycon = my_decorator(hello_pycon)
