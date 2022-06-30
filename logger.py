from datetime import datetime
from pathlib import Path


def log_decorator(directory, filename):
    p = Path.home() / directory
    p.mkdir(parents=True, exist_ok=True)
    f = p / filename
    f.touch()

    def wrapper(func):
        def inner(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            with open(f, 'a') as file:
                file.write(
                    f"Date: {start_time}\n"
                    f"Function Name: {func.__name__}\n"
                    f"Arguments: {args, kwargs}\n"
                    f"Return Value: {result}\n"
                    f"--------------------------\n"
                )

            return result

        return inner

    return wrapper
