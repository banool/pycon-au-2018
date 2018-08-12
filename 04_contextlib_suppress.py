import os

from contextlib import suppress

# Kill  process, ignore if it can't be found.
def kill_process(pid):
    try:
        os.kill(pid, signal.SIGKILL)
    except ProcessLookupError:
        pass

def kill_process(pid):
    with suppress(ProcessLookupError):
        os.kill(pid, signal.SIGKILL)


