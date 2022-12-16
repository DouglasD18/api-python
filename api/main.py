from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from api.utils import (min_digit, min_lowercase, min_size,
                       min_special_chars, min_uppercase, no_repeted)


class Rule(BaseModel):
    rule: str
    value: int


class Body(BaseModel):
    password: str
    rules: List[Rule]


app = FastAPI()


@app.post("/verify")
async def isVerified(body: Body):
    password = body.password
    rules = body.rules
    failed = []
    for rule in rules:
        if rule.rule == "minSize":
            result = min_size(password, rule.value)
            if type(result) == str:
                failed.append(result)
        elif rule.rule == "minUppercase":
            result = min_uppercase(password, rule.value)
            if type(result) == str:
                failed.append(result)
        elif rule.rule == "minLowercase":
            result = min_lowercase(password, rule.value)
            if type(result) == str:
                failed.append(result)
        elif rule.rule == "minDigit":
            result = min_digit(password, rule.value)
            if type(result) == str:
                failed.append(result)
        elif rule.rule == "noRepeted":
            result = no_repeted(password)
            if type(result) == str:
                failed.append(result)
        elif rule.rule == "minSpecialChars":
            result = min_special_chars(password, rule.value)
            if type(result) == str:
                failed.append(result)
    if len(failed) > 0:
        return {"verify": False, "noMatch": failed}
    else:
        return {"verify": True, "noMatch": failed}


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
