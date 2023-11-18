import pandas as pd
import numpy as np
import yfinance as yf
import sys
print(sys.path)


#trae los datos de las acciones de Airbnb
def read_Data():
    msft = yf.Ticker("ABNB")
    df =  msft.history(period="MAX", interval="1d")
    return df

def cambiar_a_columna_date(df):
    #cambiar_a_columna_date
    df.reset_index(inplace=True)
    # Cambiar los nombres de las columnas a minúsculas
    df = df.rename(columns=lambda x: x.lower())
    # Suponiendo que 'Date' es la columna en df que tiene las fechas en formato '2020-12-10 00:00:00-05:00'
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.strftime("%Y-%m-%d")
    df['date'] = df['date'].astype(str)

    return df

def borrar_columns(df):
    df=df.drop('dividends', axis=1)
    df=df.drop('stock splits', axis=1)
    return df



