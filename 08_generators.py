def first_n(n):
    for i in range(n):
        yield i

print("First two items from generator")
gen = first_n(5)
print(next(gen))
print(next(gen))

print()
print("Iterating through a new generator")
for i in first_n(5):
    print(i)

print()
print("[Generator] Sum of first 10 numbers")
print(sum(first_n(10)))

def first_n(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums

print()
print("[Regular] Sum of first 10 numbers")
print(sum(first_n(10)))

