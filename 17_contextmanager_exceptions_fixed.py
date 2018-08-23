from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Before")
    try:
        yield
    except Exception as e:
        print(f"Oh no: {e}")
    finally:
        print("After")

with my_context_manager():
    print(f"I love this number: {1/0}")
