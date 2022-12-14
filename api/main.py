from fastapi import FastAPI

from api.utils import verify


app = FastAPI()


@app.post("/verify")
async def isVerified(body):
    password = body["password"]
    rules = body["rules"]
    result = verify(password, rules)
    return result


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
