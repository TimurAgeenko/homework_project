from typing import Optional


def log(*, filename: Optional[str] = None) -> None:
    """
    Используется для автоматической регистрации деталей выполнения функций,
    таких как имя функции, передаваемые аргументы, результат выполнения и информация об ошибках.
    Может записывать данные в файл, если указано имя файла, либо выводить их в консоль, если имя не указано.
    """

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
