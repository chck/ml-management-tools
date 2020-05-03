from sacred import Experiment

ex = Experiment()


@ex.config
def my_config():
    recipient = "world"
    message = f"Hello {recipient}!"


@ex.automain
def my_main(message):
    print(message)
