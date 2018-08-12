from contextlib import contextmanager


@contextmanager
def FoodContextManager(data):
    print(f"Enter: {data}")
    yield data
    print(f"Exit: {data}")


with FoodContextManager({"dairy": "yuck"}) as data:
    data["fruit"] = "delicious"
