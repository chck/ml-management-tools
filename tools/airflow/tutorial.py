from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    dag_id="sample_pipeline",
    default_args={
        "start_date": datetime.now()
    },
)

task1 = BashOperator(
    task_id="print_date",
    bash_command="date",
    dag=dag,
)

task2 = BashOperator(
    task_id="echo_a",
    depends_on_past=False,
    bash_command="echo 'a'",
    dag=dag,
)

task3 = BashOperator(
    task_id="echo_b",
    depends_on_past=False,
    bash_command="echo 'b",
    dag=dag,
)

task1 >> [task2, task3]
