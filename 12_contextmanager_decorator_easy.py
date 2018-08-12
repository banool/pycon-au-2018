from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Enter!")
    yield
    print("Exit!")


with my_context_manager():
    print("Inside the block!")
