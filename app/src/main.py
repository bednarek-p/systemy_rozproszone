from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/api/get/todos/list")
async def get_todo():
    return {"todo": "This is test todo."}
