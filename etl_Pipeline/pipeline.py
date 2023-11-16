import pandas as pd
import logging
import json
#from  Database import creating_engine, disposing_engine
from airbnb.Database import database_connection,insert_Data_to_Database, read_Data_From_Database
from airbnb.transform import (
    standarizanding_Columns,
    drop_Duplicates,
    delete_Unnecesary_Columns,
    standarizanding_Names,
    delete_Special_Caracthers,
    fill_nulls,
    replace_Nulls_by0s,
    last_standarization,
    borrar_todos
)


#SPOTIFY ET

def read_csv():
    #Reading csv file
    spotify_df = pd.read_csv("airbnb/Airbnb_Open_Data3.csv")
    print("csv read succesfully")
    #logging.info("csv read succesfully")
    #
    read_Data_From_Database()
    #return spotify_df.to_json(orient='records')

read_csv()
