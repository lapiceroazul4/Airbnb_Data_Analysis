
import pandas as pd
import numpy as np
import yfinance as yf

#trae los datos de las acciones de Airbnb 
def read_Data():
    msft = yf.Ticker("ABNB")
    df =  msft.history(period="MAX", interval="1d")
    return df

def cambiar_a_columna_date(df):
    df.reset_index(inplace=True)
    return df

def borrar_columns(df):
    df=df.drop('Dividends', axis=1)
    df=df.drop('Stock Splits', axis=1)
    return df



