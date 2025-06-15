FROM apache/airflow:2.9.2

WORKDIR /students_airflow

COPY requirements.txt /students_airflow
COPY ./dags/credentials.json /students_airflow

RUN pip install -r requirements.txt