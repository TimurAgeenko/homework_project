from typing import Optional


def log(*, filename: Optional[str] = None):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} ok\n")
                else:
                    print(f"{function.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator
