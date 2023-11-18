import time
import pandas as pd
from airbnb.Database import database_connection
from kafka import KafkaProducer
from json import dumps 
from datetime import datetime, date

def kafka_producer():
    print('--------------Kafka App--------------')
    print("---------Sending Messages----------")
    conn = database_connection()
    df = pd.read_sql_query("SELECT * FROM airbnb2", conn)
    producer = KafkaProducer(
        value_serializer = lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092'],
    )
    time.sleep(1)
    try:
        for index, row in df.iterrows():
            message = row.to_dict()
            print(message)
            print("Message Sent")
            producer.send("airbnb", value=message)
            time.sleep(0.01)
    except:
        print("No hay mas mensajes")