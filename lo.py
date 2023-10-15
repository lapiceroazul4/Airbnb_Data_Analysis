import pandas as pd

empdata = pd.read_csv("Airbnb_Open_Data3.csv", low_memory=False, index_col=False, delimiter = ',')
empdata.head()
print(empdata.head())