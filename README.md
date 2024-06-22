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
- Docker

## Getting Started

1. Initialize the Airflow Environment:
`astro dev start  # Use sudo if necessary`

2. Execution Schedule:
The DAGs are scheduled to run daily at 1am UTC.
Workflow Overview:

3. A sensor checks for the availability of required CSV files.
The respective DAGs then run in parallel since they are independent.

## Running the Project

To start the project:

1. Clone this repository:
`git clone <repository_url>
cd <project_directory>`

2. Make sure the Docker Desktop is running before starting Astro CLI:
`astro dev start`

3. Access Airflow UI:
Airflow UI is available at localhost:8080 (default credentials: admin/admin).

4. Monitor DAG Runs:
Navigate to the Airflow UI to monitor and manage DAG runs.


## Additional Notes

Customize DAG scripts (dag/*.py) and utility scripts (utils/*.py) as per project requirements.
Adjust Dockerfile (Dockerfile) and configuration files (.projectConfig) based on deployment needs.