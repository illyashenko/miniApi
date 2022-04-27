import json
import jsonpickle

from fastapi import FastAPI
from srs.helpers.injector import container

app = FastAPI()


@app.get("/customers")
async def get_all():
    return container.customers_service().get_all()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
