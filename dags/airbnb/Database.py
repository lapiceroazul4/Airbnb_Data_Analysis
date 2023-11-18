import json
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

#Constantes
table='airbnb_detail'
filePath = "uk-500.csv"
filePath2 = "Airbnb_Open_Data3.csv"
createDatabase="CREATE DATABASE employee"
createDatabase2="CREATE DATABASE neighbourhoods"
dropTable='DROP TABLE IF EXISTS employee_data;'
dropTable2='DROP TABLE IF EXISTS airbnb_detail;'
sentence='''CREATE TABLE employee_data(first_name varchar(255),last_name varchar(255),company_name varchar(255),
address varchar(255),city varchar(255),county varchar(255),postal varchar(255),phone1 varchar(255),
phone2 varchar(255),email varchar(255),web varchar(255))'''
sentence2=("CREATE TABLE airbnb_detail( id  BIGINT, NAME  VARCHAR(500), host_id  VARCHAR(500), host_identity_verified "
           "VARCHAR(500), host_name VARCHAR(500), neighbourhood_group VARCHAR(500), neighbourhood VARCHAR(500), "
           "lat VARCHAR(500), `long` VARCHAR(500), country VARCHAR(500), country_code VARCHAR(500), "
           "instant_bookable VARCHAR(500), cancellation_policy VARCHAR(500), room_type VARCHAR(500), Construction_year VARCHAR("
           "500), price VARCHAR(500), service_fee VARCHAR(500), minimum_nights VARCHAR(500), number_of_reviews "
           "VARCHAR(500), last_review VARCHAR(500), reviews_per_month VARCHAR(500), "
           "review_rate_number VARCHAR(500), calculated_host_listings_count VARCHAR(500), availability_365 VARCHAR(500), "
           "house_rules VARCHAR(1400), license VARCHAR(500))")
insert="INSERT INTO employee.employee_data VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
insert2="INSERT INTO neighbourhoods.airbnb_detail VALUES ({id}, {NAME}, {host_id}, {host_name},{neighbourhood_group},{neighbourhood},{lat},{long},{country},{country_code},{instant_bookable},{cancellation_policy},{room_type},{Construction_year},{price},{service_fee},{minimum_nights},{number_of_reviews},{last_review},{reviews_per_month},{review_rate_number},{calculated_host_listings_count},{availability_365},{house_rules},{license})"
insert3="INSERT INTO neighbourhoods.airbnb_detail VALUES {}"
userDataBase = "root"
passDataBase = "Taison2023."
tableDataBase = "employee"
tableDataBase2 = "neighbourhoods"
#Constantes

def database_connection():
    try:
        conn = conn = mysql.connect(
            host='localhost',
            user='root',
            password='my-secret-pw',
            database='neighbourhoods'  # Puedes cambiar esta a tu base de datos específica
        )
        return conn
    except Error as e:
        print("Error while connecting to MySQL", e)

def insert_Data_to_Database(df_airbnb):
    conn=database_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute(dropTable2)
        print('Creating table....')
        # in the below line please pass the creation table statement which you want #to create
        cursor.execute(sentence2)
        print("Table is created....")
        iter=0
        # loop through the data frame
        for i, row in df_airbnb.iterrows():
            # here %S means string values
            #print(len(tuple(row)))
            #print(insert3.format(tuple(row)).replace(", nan",', "nan"'))
            cursor.execute(insert3.format(tuple(row)).replace(", nan",', Null'))
            if iter == 1000:
                print(f"Record inserted {(i/df_airbnb.shape[0])*100}%")
                iter=0
            # the connection is not auto committed by default, so we must commit to save our changes
            iter+=1
            conn.commit()
        print(f"Record inserted {(i/df_airbnb.shape[0])*100}%")


def read_Data_From_Database():
    print("yes")
    conn=database_connection()
    query=f'select * from {table}'
    df_airbnb=pd.read_sql(query,conn)
    print(df_airbnb)
    return df_airbnb

#df_airbnb=pd.read_csv("Airbnb_Open_Data3.csv", low_memory=False, na_values=[''])
#print(df_airbnb.head(2))
#insert_Data_to_Database(df_airbnb)
#ead_Data_From_Database()
