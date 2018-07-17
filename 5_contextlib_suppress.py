import os
import signal

from contextlib import suppress


def kill_process(pid):
    # Kill a process, ignore if it can't be found.
    with suppress(ProcessLookupError):
        os.kill(pid, signal.SIGKILL)
