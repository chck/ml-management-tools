import hydra
from omegaconf import DictConfig


@hydra.main(config_path="config.yaml")
def my_app(cfg: DictConfig) -> None:
    print(cfg.pretty())
    params = cfg.model
    print(params)
    # model = get_model(params)
    # model.fit(X, y)
    # return r2_score(model.predict(X), y)


if __name__ == "__main__":
    my_app()
