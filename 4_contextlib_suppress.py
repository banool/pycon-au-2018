import os
import signal

from contextlib import suppress


def kill_process(pid):
    # Kill a process, ignore if it can't be found.
    with suppress(ProcessLookupError):
        os.kill(pid, signal.SIGKILL)

# Much nicer than:
def kill_process(pid):
    try:
        os.kill(pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
