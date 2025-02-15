from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'data-platform',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_platform_pipeline',
    default_args=default_args,
    description='Orchestrates the data pipeline using Apache Airflow',
    schedule_interval=timedelta(days=1),  # Adjust scheduling as needed
)

t1 = BashOperator(
    task_id='run_ingestion',
    bash_command='bash $(pwd)/scripts/run_ingestion.sh',
    dag=dag,
)

t2 = BashOperator(
    task_id='run_staging',
    bash_command='bash $(pwd)/scripts/run_staging.sh',
    dag=dag,
)

t3 = BashOperator(
    task_id='run_processing',
    bash_command='bash $(pwd)/scripts/run_processing.sh',
    dag=dag,
)

t4 = BashOperator(
    task_id='run_analytics',
    bash_command='bash $(pwd)/scripts/run_analytics.sh',
    dag=dag,
)

# Define task dependencies: ingestion -> staging -> processing -> analytics
t1 >> t2 >> t3 >> t4
