from concurrent.futures import ThreadPoolExecutor

data = {
    "Watermelon": "delicious",
    "Fruit": "spectacular",
    "Dairy": "yucky",
    "Meat": "not cool",
}


def myfunc(noun, adjective):
    return f"{noun} is {adjective}!"

# Bad!!!
pool = ThreadPoolExecutor()
for k, v in data.items():
    pool.submit(myfunc, k, v)
# Wait on the results and do something with them.
pool.shutdown()

# Good, safe, context managed!
with ThreadPoolExecutor() as pool:
    for k, v in data.items():
        pool.submit(myfunc, k, v)
    # Wait on the results and do something with them.

for k, v in data.items():
    print(make_a_sentence(k, v))

# Spinach is delicious!
# Fruit is spectacular!
# Dairy is yucky!
# Meat is not cool!
