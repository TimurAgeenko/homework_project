import tempfile

from src.decorators import log

with tempfile.TemporaryFile(mode="r+") as temp_file:

    def test_log():
        @log(filename=temp_file.name)
        def add_numbers(a, b):
            return a + b

        result = add_numbers(1, 2)
        with open(temp_file.name) as file:
            assert file.read() == "add_numbers ok\n"

    def test_log_error():
        @log(filename=temp_file.name)
        def add_numbers(a, b):
            if not isinstance(a, int) or not isinstance(b, int):
                raise TypeError("Аргументы должны иметь тип int")
            return a + b

        result = add_numbers("1", 2)
        with open(temp_file.name) as file:
            assert file.read() == (
                "add_numbers ok\n" "add_numbers error: Аргументы должны иметь тип int. Inputs: ('1', 2), {}\n"
            )


def test_log_print(capsys):
    @log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n"


def test_log_error_print(capsys):
    @log()
    def add_numbers(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Аргументы должны иметь тип int")
        return a + b

    result = add_numbers("1", 2)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers error: Аргументы должны иметь тип int. Inputs: ('1', 2), {}\n"
