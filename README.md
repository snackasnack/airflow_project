# airflow_project

This repository contains an Apache Airflow project initialized using Astro CLI (astro dev init). The project orchestrates data workflows using DAGs (Directed Acyclic Graphs) defined in Python scripts.

## Project Structure

- raw_files/: Directory to store raw CSV files used exclusively for this project.
- dag/: Contains Python scripts defining Airflow DAGs.
- utils/: Utility scripts for general purposes.
- Dockerfile: Modified to include necessary project files (DAGs, configuration scripts).
- .projectConfig: Configuration file containing directory information for raw and processed files.

## Prerequisites

Ensure you have the following installed:
- Python 3
- Docker (https://www.docker.com/products/docker-desktop/)
- Astro CLI (https://www.astronomer.io/docs/astro/cli/overview)

## Running the Project

To start the project:

1. Clone this repository:
`git clone https://github.com/snackasnack/airflow_project.git
cd airflow_project`

2. Make sure the Docker Desktop is running before starting Astro CLI:
`astro dev start`

3. Access Airflow UI:
Airflow UI is available at localhost:8080 (default credentials: admin/admin).

4. Monitor DAG Runs:
Navigate to the Airflow UI to monitor and manage DAG runs.

5. Getting output files from scheduler container:
`docker cp <container-id> /usr/local/airflow/processed_files/processed_dataset1.csv <download_directory>`

## Additional Notes
1. Execution Schedule:
The DAGs are scheduled to run daily at 1am UTC.
2. Customize DAG scripts (dag/*.py) and utility scripts (utils/*.py) as per project requirements.
3. Adjust Dockerfile (Dockerfile) and configuration files (.projectConfig) based on deployment needs.
