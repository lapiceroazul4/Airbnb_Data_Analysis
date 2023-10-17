
import pandas as pd
import numpy as np
import yfinance as yf

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
    return df

def borrar_columns(df):
    df=df.drop('dividends', axis=1)
    df=df.drop('stock splits', axis=1)
    return df



