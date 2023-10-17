import psycopg2
from api-yf-transform import cambiar_a_columna_date, borrar_columns, read_data

# Parámetros de conexión
db_params = {
    "host": "localhost",          # La dirección IP o el nombre de host del contenedor
    "port": "5435",               # El puerto mapeado del contenedor (5435)
    "database": "postgres",       # Nombre de la base de datos (por defecto)
    "user": "postgres",           # Usuario de la base de datos
    "password": "mysecretpass",   # Contraseña del usuario
}


def transform():
    df=read_data()
    df_previo =cambiar_a_columna_date(df)
    df_final =borrar_columns(df_previo)
    print(df_final)

# Intentar conectarse a la base de datos
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Ejecutar consultas aquí
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Conexión exitosa a PostgreSQL:", version)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS apiyahoofinace (
    Date DATE,
    Open DOUBLE PRECISION,
    High DOUBLE PRECISION,
    Low DOUBLE PRECISION,
    Close DOUBLE PRECISION,
    Volume INTEGER
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    
    
    # Consultar el catálogo information_schema para obtener las tablas
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cursor.fetchall()

    # Imprimir las tablas
    print("Tablas en la base de datos:")
    for table in tables:
        print(table[0])
    # Confirmar los cambios
    connection.commit()

    # Cerrar la conexión
    cursor.close()
    connection.close()

except Exception as e:
    print("Error de conexión:", e)