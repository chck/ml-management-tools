import lightgbm as lgb
from sklearn import datasets
from sklearn.model_selection import train_test_split
import mlflow
import os

params = dict(
    test_size=0.2,
    random_state=3,
)

iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, **params)

lgb_params = dict(
    learning_rate=0.05,
    n_estimators=500,
)
model = lgb.LGBMClassifier(**lgb_params)

def mlflow_callback():
    def callback(env):
        for name, loss_name, loss_value, _ in env.evaluation_result_list:
            mlflow.log_metric(key=loss_name, value=loss_value, step=env.iteration)
    return callback

mlflow.set_tracking_uri(os.environ["MLFLOW_HOST"])
mlflow.set_experiment("MLMAN-1")
with mlflow.start_run():
    mlflow.log_params({**params, **lgb_params})
    model.fit(
        X_train,
        y_train,
        eval_set=(X_test, y_test),
        eval_metric=["softmax"],
        callbacks=[
            lgb.early_stopping(10),
            mlflow_callback(),
        ])

    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("Hello world!")
    mlflow.log_artifact("output.txt")
