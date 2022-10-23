import json

from fastapi import FastAPI

from database import Database
from todo import Todo

app = FastAPI()
postgres_db = Database("database_postgres", "prisma", "postgres", "postgres", "5432")


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/api/get/todo/{id}")
async def get_todo(id: int):
    record = postgres_db.get_record_by_id(id)
    return {"id": record[0], "name": record[1], "status": record[2]}


@app.get("/api/get/todos/list")
async def get_todos_list():
    json_list = [{"id": record[0], "name": record[1], "status": record[2]} for record in postgres_db.get_all_records()]
    sorted_json_list = sorted(json_list, key=lambda dict: dict["id"])
    return sorted_json_list


@app.post("/api/create/todo")
async def create_todo(todo: Todo):
    postgres_db.insert_into_todos(todo.name, todo.status)
    return {"name": todo.name, "status": todo.status}


@app.post("/api/update/todo/{id}")
async def update_todo(id: int, todo: Todo):
    postgres_db.update_record_by_id(id, todo.name, todo.status)
    return {"name": todo.name, "status": todo.status}


@app.post("/api/delete/todo/{id}")
async def delete_todo(id: int):
    deleted_record = postgres_db.get_record_by_id(id)
    postgres_db.delete_record_by_id(id)
    return deleted_record


def main():
    postgres_db.init_todos_table()
    print("##########################################################")
    postgres_db.insert_into_todos("Task nr 1", "To-do")
    postgres_db.insert_into_todos("Task nr 2", "To-do")


if __name__ == "__main__":
    main()
