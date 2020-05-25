from sacred.experiment import Experiment

ex = Experiment('named_configs_demo')


@ex.config
def cfg():
    a = 10
    b = 3 * a
    c = "foo"


@ex.named_config
def variant1():
    a = 100
    c = "bar"


@ex.main
def my_main(a: int):
    print(a)


if __name__ == "__main__":
    ex.run_commandline()
