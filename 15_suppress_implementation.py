class suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc, exc_tb):
        return (
            exc_type is not None and 
            issubclass(exc_type, self.exceptions)
        )
