from sacred import Experiment
from sacred.observers import FileStorageObserver
from neptunecontrib.monitoring.sacred import NeptuneObserver
import os
import warnings
warnings.filterwarnings('ignore')

ex = Experiment("elastic_net")

# ex.observers.append(FileStorageObserver("sacredruns"))
ex.observers.append(NeptuneObserver(api_token=os.environ["NEPTUNE_API_TOKEN"],
                                    project_name=os.environ["NEPTURE_PROJECT_NAME"]))

@ex.config
def parameters():  # Declare default parameters
    alpha = 0.0005
    l1_ratio = 0.9
    random_state = 3

@ex.capture
def get_model(alpha: float, l1_ratio: float, random_state: int):
    from sklearn.linear_model import ElasticNet
    return ElasticNet(
        alpha=alpha,
        l1_ratio=l1_ratio,
        random_state=random_state,
    )

@ex.main
def run():
    model = get_model()  # Parameters are injected implicitly.
    model.fit(X, y)
    return r2_score(model.predict(X), y)

ex.run()
