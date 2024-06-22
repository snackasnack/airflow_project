from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os
from process_csv import process_csv, save_csv
from utils import read_config


# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 22),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'process_csv_files',
    default_args=default_args,
    description='A DAG to process CSV files',
    schedule_interval='0 1 * * *',
)

# Read the configuration file
config_file_path = '/usr/local/airflow/.projectConfig'
config = read_config(config_file_path)

# Define the Python callables for processing and saving CSV files
def process_and_save_dataset(file_path, output_path):
    processed_df = process_csv(file_path)
    save_csv(processed_df, output_path)

# Define the task groups for each dataset
process_dataset1_task = PythonOperator(
    task_id='process_dataset1',
    python_callable=process_and_save_dataset,
    op_args=[config['dataset1_path'], config['processed_dataset1_path']],
    dag=dag,
)

process_dataset2_task = PythonOperator(
    task_id='process_dataset2',
    python_callable=process_and_save_dataset,
    op_args=[config['dataset2_path'], config['processed_dataset2_path']],
    dag=dag,
)

# Set the task dependencies (if any)
process_dataset1_task
process_dataset2_task
