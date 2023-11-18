from kafka import KafkaConsumer
import requests
import re
import pandas as pd
from json import loads
from datetime import datetime, date
import json
API_ENDPOINT = "https://api.powerbi.com/beta/693cbea0-4ef9-4254-8977-76e05cb5f556/datasets/7b1b618b-a856-4131-939e-c46249fbe35a/rows?experience=power-bi&key=Ojhelk%2BjKA9Fg3p%2BE78IWB7hcNuY1S1RheQiZNT2NMdTt1tUBZI6BFarAesW3%2BbY7I0wRGEopHvW%2Fk%2B2AREJNw%3D%3D"

print("Kafka Consumer App Inicia")
consumer = KafkaConsumer(
        'soccer',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=[f'localhost:9092']
    )
consumer.poll()
consumer.seek_to_end()

for data_json in consumer:
    s = data_json.value
    df = pd.DataFrame.from_dict([s])
    data = bytes(df.to_json(orient='records'), 'utf-8')
    print(data)
    req = requests.post(API_ENDPOINT, data)

"""
https://api.powerbi.com/beta/693cbea0-4ef9-4254-8977-76e05cb5f556/datasets/7b1b618b-a856-4131-939e-c46249fbe35a/rows?experience=power-bi&key=Ojhelk%2BjKA9Fg3p%2BE78IWB7hcNuY1S1RheQiZNT2NMdTt1tUBZI6BFarAesW3%2BbY7I0wRGEopHvW%2Fk%2B2AREJNw%3D%3D

[
{
"price" :98.6,
"service_fee" :98.6,
"numbers_of_reviews" :98.6,
"neighbourhood_group" :"AAAAA555555"
}
]
"""