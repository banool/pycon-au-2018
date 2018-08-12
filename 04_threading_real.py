from concurrent.futures import (
    as_completed,
    ThreadPoolExecutor,
)

data = {
    "Watermelon": "delicious",
    "Fruit": "spectacular",
    "Dairy": "yucky",
    "Meat": "not cool",
}


def myfunc(noun, adjective):
    return f"{noun} is {adjective}!"


with ThreadPoolExecutor() as pool:
    futures = []
    for k, v in data.items():
        future = pool.submit(myfunc, k, v)
        futures.append(future)
    # Wait on the results and do something with them.
    for future in as_completed(futures):
        print(future.result())

# pool.submit(myfunc, "Bread", "neat")
