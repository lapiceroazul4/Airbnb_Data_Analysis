from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pipeline import read_data_from_airbnb_Database, read_data_from_api_yahoo_finance, transform_Airbnb_Dataset, transform_Yahoo_Finance_Api,load_db,load_api,kafka

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 8),  # Update the start date to today or an appropriate date
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    'etl_dag',
    default_args=default_args,
    description='Workshop #2',
    schedule_interval='@daily',  # Set the schedule interval as per your requirements
) as dag:

    read_data_from_airbnb_Database = PythonOperator(
        task_id='read_data_from_airbnb_Database',
        python_callable=read_data_from_airbnb_Database,
    )

    read_data_from_api_yahoo_finance = PythonOperator(
        task_id='read_data_from_api_yahoo_finance',
        python_callable=read_data_from_api_yahoo_finance,
        )
    
    transform_Airbnb_Dataset = PythonOperator(
        task_id='transform_Airbnb_Dataset',
        python_callable=transform_Airbnb_Dataset,
    )

    transform_Yahoo_Finance_Api = PythonOperator(
        task_id='transform_Yahoo_Finance_Api',
        python_callable=transform_Yahoo_Finance_Api,
        )
    
    load_db = PythonOperator(
        task_id ='load_db',
        python_callable = load_db,
        provide_context = True,
    )
    load_db = PythonOperator(
        task_id ='load_api',
        python_callable = load_db,
        provide_context = True,
    )

    kafka = PythonOperator(
        task_id ='kafka',
        python_callable = kafka,
        provide_context = True,
    )
    
    read_data_from_api_yahoo_finance >> read_data_from_api_yahoo_finance >> load_api >> kafka
    read_data_from_airbnb_Database >> transform_Yahoo_Finance_Api >> load_db >> kafka
