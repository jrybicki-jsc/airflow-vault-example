FROM python:3.9-slim
EXPOSE 8080

RUN python -m pip install apache-airflow==2.2.3 apache-airflow-providers-ssh==2.3.0 apache-airflow-providers-hashicorp

CMD airflow standalone 
