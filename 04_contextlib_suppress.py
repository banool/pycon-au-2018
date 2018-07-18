import os

from contextlib import suppress


def remove_file(path):
    # Remove a file, ignore if it can't be found.
    with suppress(FileNotFoundError):
        os.remove(path)


# More succinct than:
def remove_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
