def call_for_help():
    print("Getting help!!!")

class MyContextManager:
    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc, exc_tb):
        if exc:
            print("Oh no! Calling for help then re-raising!")
            call_for_help()
            return False

with MyContextManager():
    print(f"Look at this sweet number: {1/0}")
