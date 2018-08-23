from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Before")
    yield
    print("After")

with my_context_manager():
    print(f"I love this number: {1/0}")
