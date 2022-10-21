import psycopg2
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/api/get/todos/list")
async def get_todo():
    return {"todo": "This is test todo."}


hostname = "database_postgres"
database = "prisma"
username = "postgres"
password = "postgres"
port_id = 5432


try:
    connection = psycopg2.connect(host=hostname, dbname=database, user=username, password=password, port=port_id)
    cursor = connection.cursor()

    create_script = """ CREATE TABLE IF NOT EXISTS todos (
                                    id      int PRIMARY KEY,
                                    name    varchar(100) NOT NULL,
                                    status  varchar(40) NOT NULL)"""
    cursor.execute(create_script)

    connection.commit()
except Exception as err:
    print(err)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
