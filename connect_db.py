import os
import psycopg2

POSTGRES_HOSTNAME = os.getenv('POSTGRES_HOSTNAME')
POSTGRES_PORT = os.getenv('POSTGRE_PORT')
POSTGRES_USERNAME = os.getenv('POSTGRE_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRE_PASSWORD')
POSTGRES_DBNAME = os.getenv('POSTGRE_DBNAME')

psyco = None
cursor = None

try:
    psyco = psycopg2.connect(
        host = POSTGRES_HOSTNAME,
        user = POSTGRES_USERNAME,
        password = POSTGRES_PASSWORD,
        database = POSTGRES_DBNAME,
    )

    cursor = psyco.cursor()

    cursor.excute("SELECT * FROM users")

    for row in cursor.fetchali():
        print(row)

    
    cursor.close()
    psyco.close()

except Exception as e:
    print(e)
finally:
    print("Done")
