import os
from sys import exit

blah = []
for i in os.listdir():
    if i.startswith("0") or i.startswith("1"):
        blah.append(i)

blah = sorted(blah)
top = len(blah)

ops = []
for idx, i in enumerate(blah):
    suffix = '_'.join(i.split('_')[1:])
    new = "{:02d}_{}".format(idx+1, suffix)
    ops.append((i, new))

print(ops)
conf = input("Do you wanna do this shit? [y/n] ")[0]

if conf != "y":
    print("alright cya")
    exit()

for old, new in ops:
    if old != new:
        os.rename(old, new)
