from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello World!"

@app.get("/greet/{name}")
def greet(name: str):
    return f"Good Afternoon, {name.title()}!"