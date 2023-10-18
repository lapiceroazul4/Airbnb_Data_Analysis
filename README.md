# Workshop_spotify

**Descripción del Proyecto**: "implementaremos la API de Yahoo Finance para obtener datos financieros de Airbnb y almacenarlos en una base de datos PostgreSQL que se ejecuta en un contenedor Docker".

## Requisitos
- Python 3.11.6
- Docker
- PostgreSQL (ejecutado en un contenedor de Docker)


## Estructura del Proyecto

- **docker-compose.yml**: Archivo de configuración de Docker Compose para crear y gestionar contenedores Docker de Airflow.

- **/dags**: Contiene los archivos de DAG de Apache Airflow. Los archivos `.py` que orquestan el proceso ETL se encuentran aquí.

  

# Ejecución del Proyecto
## Paso 1:Clone el repositorio .
```bash
https://github.com/lapiceroazul4/Airbnb_Data_Analysis.git
```
## Paso 2: Instalamos la Api de Yahoo Finance.
```bash
pip install yfinance
```
## Paso 3: Instalamos las dependencias necesarias.
```bash
pip install psycopg2
pip install sqlalchemy
```
## Paso 4: Corremos el contenedor de Docker.
```bash
sudo docker run -d --name=postgres -p 5435:5432 -v postgres-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpass postgres
```
## Paso 5: Entramos a la carpeta de la Api.
```bash
cd api_yahoo_finance
```
## Paso 6: Puedes mirar el Eda y/o Correr el proyecto

```bash
python load.py
```




