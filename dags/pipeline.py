import pandas as pd
import logging
import json
from airbnb.Database import database_connection,insert_Data_to_Database, read_Data_From_Database
from airbnb.transform import standarizanding_Columns,drop_Duplicates,delete_Unnecesary_Columns,standarizanding_Names,delete_Special_Caracthers,fill_nulls,last_standarization,borrar_todos
from api_yahoo_finance.api_yf_transform import borrar_columns, read_Data , cambiar_a_columna_date

def read_data_from_airbnb_Database():
    #Reading csv file
    df_airbnb = pd.read_csv("airbnb/Airbnb_Open_Data3.csv")
    print("csv read succesfully")
    logging.info("csv read succesfully")
    #return spotify_df.to_json(orient='records')
    df_airbnb=read_Data_From_Database()
    return df_airbnb.to_json(orient='records')

def read_data_from_api_yahoo_finance():
    #Reading csv file
    df=read_Data()
    print(df)
    return df
    logging.info("csv read succesfully")
    return df.to_json(orient='records')

def transform_Airbnb_Dataset(**kwargs):
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="read_data_from_airbnb_Database")
    json_data = json.loads(str_data)
    spotify_df = pd.json_normalize(data=json_data)

    df_airbnb = standarizanding_Columns(df_airbnb)
    df_airbnb = delete_Unnecesary_Columns(df_airbnb)
    df_airbnb = drop_Duplicates(df_airbnb)
    df_airbnb = standarizanding_Names(df_airbnb)
    df_airbnb = delete_Special_Caracthers(df_airbnb)
    df_airbnb = fill_nulls(df_airbnb)
    df_airbnb = last_standarization(df_airbnb)
    df_airbnb = borrar_todos(df_airbnb)
    return df_airbnb.to_json(orient='records')


def transform_Yahoo_Finance_Api(**kwargs):
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="read_data_from_api_yahoo_finance")
    json_data = json.loads(str_data)
    grammys_df = pd.json_normalize(data=json_data)
    logging.info(f"data from db has started Yahoo Finance transformation proccess")
    df=cambiar_a_columna_date(df)
    df=borrar_columns(df)
    return df.to_json(orient='records')

def merge():
    df=read_data_from_api_yahoo_finance()
    df=transform_YahoFinance_Api(df)
    print(df)
    df_airbnb=read_data_from_airbnb_Database()
    df_airbnb=transform_Airbnb_Dataset(df_airbnb)
    print(df_airbnb)
    # Merge de los DataFrames usando la columna de fechas 'Date' y 'last_review'
    merged_df = pd.merge(df, df_airbnb, left_on='date', right_on='last_review', how='inner')
    print(merged_df)

data=read_data_from_api_yahoo_finance()
data_data=read_data_from_airbnb_Database()
print(data)
print(data_data)
#merge()
#df_airbnb=read_Data_From_Database()
#print("yes")
#transform_Airbnb_Dataset(df_airbnb)
#read_csv()
