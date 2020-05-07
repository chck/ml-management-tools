from sacred import Experiment

ex = Experiment()


@ex.config
def my_config() -> None:
    recipient = "world"
    f"Hello {recipient}!"


@ex.automain
def my_main(message: str) -> None:
    print(message)
