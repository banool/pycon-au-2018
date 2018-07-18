class FoodContextManager:
    def __init__(self):
        self.data = {}

    def __enter__(self):
        print(f"Enter: {self.data}")
        return self.data

    def __exit__(self, *exc):
        print(f"Exit: {self.data}")


with FoodContextManager() as data:
    data["fruit"] = "delicious"
