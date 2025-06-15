from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from gsheet_pipeline import *


default_args = {
    'owner': 'Obinna',
    'start_date': datetime(2025, 6, 15, 2),
    'schedule_interval': '@daily',
    'retries': 3
}

etl_dag = DAG(
    dag_id='gsheet_pipeline',
    default_args=default_args
)


students_pipeline = PythonOperator(
    task_id = 'ingest_and_load',
    python_callable = load_to_s3,
    dag = etl_dag
)



students_pipeline