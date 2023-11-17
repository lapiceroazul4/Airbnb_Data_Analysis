import pandas as pd
import numpy as np

def standarizanding_Columns(df_airbnb):
    columna_float = ["lat", "long", "Construction_year", "minimum_nights", "number_of_reviews", "reviews_per_month", "review_rate_number", "calculated_host_listings_count", "availability_365"]
    df_airbnb[columna_float] = df_airbnb[columna_float].astype('float64')
    df_airbnb['host_id'] = df_airbnb['host_id'].astype('int64')
    #df_airbnb["construction_year"] = df_airbnb["construction_year"].astype(int)
    return df_airbnb

def drop_Duplicates(df_airbnb):
    df_airbnb = df_airbnb.drop_duplicates()
    return df_airbnb

def delete_Unnecesary_Columns(df_airbnb):
    df_airbnb.drop(["license", "country", "country_code"], axis=1, inplace=True)
    return df_airbnb

def standarizanding_Names(df_airbnb):
    new_column_names = [x.lower().replace(" ", "_") for x in df_airbnb.columns]
    df_airbnb.columns = new_column_names
    return df_airbnb

def delete_Special_Caracthers(df_airbnb):
    df_airbnb["price"] = df_airbnb["price"].str.replace('$', '').str.replace(',', '').str.strip()
    df_airbnb["service_fee"] = df_airbnb["service_fee"].str.replace('$', '').str.replace(',', '').str.strip()
    return df_airbnb

def fill_nulls(df_airbnb):

    ### Limpia los valores no finitos en la columna "Construction year
    df_airbnb["construction_year"] = df_airbnb["construction_year"].replace([np.inf, -np.inf], np.nan)
    df_airbnb["construction_year"] = df_airbnb["construction_year"].fillna(0)
    # Rellenar valores nulos con 0 o el valor
    # Rellenar valores nulos con 0 o el valor
    ##fill number_of_reviews
    df_airbnb.loc[df_airbnb["number_of_reviews"] == 0, "last_review"] = 0
    df_airbnb.loc[df_airbnb["number_of_reviews"] == 0, "reviews_per_month"] = 0

    df_airbnb["host_identity_verified"].fillna("unverified", inplace=True)

    ## fill_nulls_of house_rules
    df_airbnb["house_rules"] = df_airbnb["house_rules"].fillna("No se Especificaron Las Reglas")

    #Quitamos los valores nulos del host name
    df_airbnb["host_name"].fillna("no provided")

    #Admitimos solo valores positivos para la columna minimum nights
    df_airbnb["minimum_nights"] = df_airbnb["minimum_nights"].abs()
    return df_airbnb

def last_standarization(df_airbnb):
    df_airbnb["name"] = df_airbnb["name"].str.replace(r'[^a-zA-Z\s]', '', regex=True)
    df_airbnb["house_rules"] = df_airbnb["house_rules"].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    df_airbnb["host_name"] = df_airbnb["host_name"].str.replace(r'[^a-zA-Z\s]', '', regex=True)

    #df_airbnb['last_review'] = pd.to_datetime(df_airbnb['last_review'])
    return df_airbnb

def borrar_todos(df_airbnb):
    df_airbnb=df_airbnb.dropna()
    return df_airbnb


