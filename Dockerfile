FROM quay.io/astronomer/astro-runtime:11.5.0

COPY dags /usr/local/airflow/dags
COPY raw_files /usr/local/airflow/raw_files
COPY .projectConfig /usr/local/airflow