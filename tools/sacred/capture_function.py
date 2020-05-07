from sacred import Experiment
from sacred.utils import apply_backspaces_and_linefeeds

ex = Experiment("my_experiment")

ex.captured_out_filter = apply_backspaces_and_linefeeds


@ex.config
def my_config() -> None:
    pass


@ex.capture
def some_function(a: int, foo: int, bar: int = 10) -> None:
    print(a, foo, bar)


@ex.main
def my_main() -> None:
    some_function(1, 2, 3)  # 1 2 3
    some_function(1)  # 1 42 'baz'
    some_function(1, bar=12)  # 1 42 12
    some_function()  # TypeError: missing value for 'a'


if __name__ == "__main__":
    ex.run_commandline()
