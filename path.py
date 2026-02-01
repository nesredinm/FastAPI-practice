from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to consistency"}


@app.get("/tipes/{tip_1}") # -> this is path decorator.
def tip(tip_1:str):
    return {"tip_1": f"Here is your {tip_1}: Stay Positive"}