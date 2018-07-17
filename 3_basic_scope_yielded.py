with open("myfile.txt") as f:
    pass
content = f.read()
print(content)
# ValueError: I/O operation on closed file.
