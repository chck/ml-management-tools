from sacred import Experiment

ex = Experiment()

@ex.automain
def my_main():
    print("Hello world!")
