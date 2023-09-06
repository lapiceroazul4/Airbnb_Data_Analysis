## Exploring the Dataset

---

- **Columns Description**
    - **id →** Airbnb's unique identifier for the listing
    - **name** → Airbnb's name
    - **Host_id** → Airbnb's unique identifier for the host/user
    - **Host_identity_verified** → is a boolean, t=true; f=false
    - **Host_name** → Name of the host, Usually just the first name(s).
    - **neighbourhood group** → The group of the neighbourhood
    - **neighbourhood** → The neighbourhood
    - **latitude** → the latitude of the place
    - **longitude** → the longitude of the place
    - **country** → by default USA
    - **country code** → by default US
    - **instant_bookable** → is a boolean
    - **cancellation policy** → can be (strict, moderate, flexible)
    - **room type** → can be (private room, entire home/apt
    - **construction year** → the year it was constructed
    - **price** → the price in US dollars
    - **service fee** → in US dollars
    - **minimum night** → the amount of minimum nights
    - **number of reviews** → how many reviews it has
    - **last_review** → when was the last review
    - **reviews_per_month** → the average reviews by month
    - **review rate number** → the number of reviews rate
    - **availability 365** → the number of days it is avalaible if it's the whole year, then 365
    - **house_rules** → some of the host's rules

## Keep in mind…

All the information comes from a Kaggle CSV file. To align with the professor's request, we must upload this CSV to a database before starting the Exploratory Data Analysis (EDA).

# Exploratory Data Analysis (EDA) Process

## Importing Libraries

The following libraries are imported for data analysis:

- `pandas`: for data manipulation
- `numpy`: for numerical operations
- `seaborn`: for data visualization
- `Database`: custom module for database operations

## Data Preprocessing

### Reading the CSV File

The dataset is read from a CSV file named `"Airbnb_Open_Data.csv"` into a pandas dataframe.

### Data Cleansing

Several data cleansing steps are performed to prepare the dataset for uploading into a Mongo’s database

- Special characters and numbers are removed from certain columns, such as `"NAME,"` `"house_rules,"` and `"host name."`
- Columns that do not contribute significantly to the analysis are dropped, including `"license,"` `"country,"` and `"country code."`
- Null values in the `"host name"` column are filled with `"no provided."`
- Only positive values are retained in the `"minimum nights"` column.
- Duplicates are not present in this Dataset
- The cleansed data is saved to a new CSV file named `"import.csv"` and uploaded to a Mongo’s database table named `"airbnbs."`

## Data Types and Missing Values

The data types of variables in the dataset are examined, and it is determined how many variables of each data type are present. The dimensions of the dataset are also explored. Additionally, the presence of explicit null values in the dataset is checked, and the count of null values per variable is calculated. The proportion of missing values per variable is visualized using a histogram. Finally, the total count of missing values in the dataset is determined.

## Data Cleaning

### Standardizing Column Names

Column names are standardized by converting them to lowercase and replacing spaces with underscores.

### Handling Missing Values

Missing values in the `"host_identity_verified"` column are filled with `"unverified."`

### Removing Dollar Symbols

Dollar symbols are removed from the `"price"` and `"service_fee"` columns, and the columns are converted to float data type.

### Cleaning "Construction Year" Column

Non-finite values in the `"Construction year"` column are replaced with NaN, and missing values are filled with zeros. The data type of this column is changed to integer.

### Replacing Null Values in "last_review" and "reviews_per_month"

Null values in the `"last_review"` and `"reviews_per_month"` columns are replaced with zeros when the `"number_of_reviews"` is zero.

### Replacing Null Values in "house_rules"

Null values in the `"house_rules"` column are replaced with `"No se Especificaron Las Reglas."`

## Creating Dimensions for Datawarehouse

Several dimensions are created from the original dataset in order to make a DataWarehouse:

### Neighbourhood Table

A table containing information about neighborhoods is created, including neighborhood group, neighborhood, latitude, and longitude.

### Host Table

A table containing information about hosts is created, including host ID, host name, and host identity verification status.

### Airbnb Detail Table

A table containing detailed information about Airbnb listings is created, including listing ID, name, instant bookable status, cancellation policy, room type, construction year, price, service fee, minimum nights, number of reviews, last review date, reviews per month, review rate number, calculated host listings count, availability, and house rules.

## Transformations on the Neighbourhoods Dimension

### Grouping and Aggregating Neighbourhood Data

Neighborhood data is grouped to remove redundancy and calculate the average latitude and longitude for each neighborhood group and neighborhood.

### Adding a Neighbourhood ID

A numerical identifier is added to each neighborhood for easy reference.

## Data Cleaning (Fact Table)

Once the new dimensions are created, the first dataframe is adjust to become a Fact Table.

### Removing Redundant Columns

Columns that are already included in the newly created dimensions, such as `"neighbourhood_group,"` `"neighbourhood,"` `"host_name,"` and `"host_identity_verified,"` are dropped from the main dataset.

## Data Loading

Finally, the cleansed and transformed data is loaded into a database for further analysis. A database engine and session are created for this purpose.

## Problems While Developing

While uploading the csv to the DB, we’ve found a error after importing succesfully over 40.000 rows 

The error message indicates that there was an issue with the data being inserted into the "host name" column of the "airbnbs" table in the database. Specifically the error says "\xE2\x80\x86Ai," is causing the error.

After looking for a solution on internet we found that this error is typically related to character encoding issues. It seems like the data contains special characters or non-standard characters that are not supported by the character encoding of the database column. However, we haven’t solved the problem because all the columns appers to be properly encoded.

## Github

- https://github.com/lapiceroazul4/Airbnb_Data_Analysis
