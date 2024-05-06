# File: main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
async def add_numbers(x: int, y: int):
    return {"result": x + y}
