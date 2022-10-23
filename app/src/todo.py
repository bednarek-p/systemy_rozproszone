from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    status: str


if __name__ == "__main__":
    pass
