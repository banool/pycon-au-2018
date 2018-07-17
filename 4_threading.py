from concurrent.futures import ThreadPoolExecutor

data = {
    "Spinach": "delicious",
    "Fruit": "spectacular",
    "Dairy": "yucky",
    "Meat": "not cool",
}


def make_a_sentence(noun, adjective):
    return f"{noun} is {adjective}!"


# Bad!!!
pool = ThreadPoolExecutor()
for k, v in data.items():
    pool.submit(make_a_sentence, k, v)
# Wait on the results and do something with them.
pool.shutdown()

# Good, safe, context managed!
with ThreadPoolExecutor() as pool:
    for k, v in data.items():
        pool.submit(make_a_sentence, k, v)
    # Wait on the results and do something with them.

for k, v in data.items():
    print(make_a_sentence(k, v))
