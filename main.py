from typing import Optional
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    """
    root function with concurrency
    :return:
    """
    return {
        "message": "Hello Krishna!"
    }

@app.get("/user_details")
async def get_user():
    """
    Get the user details
    :return:
    """
    return {
        "message":"Hello Jagannath"
    }

@app.get("/hello/{user_name}")
async def get_user_id(user_name):
    """
    get the user description
    :param user_name:
    :return: User Description
    """
    return {
        "user_description":user_name+" "+ "is GREAT"
    }

@app.get("/normal")
def root_normal():
    """
    Normal root function
    :return:
    """
    return {"message": "Hello World"}


@app.get("/items/{item_id:int}")
async def read_item(item_id):
    """
    Read the item id
    :param item_id:
    :return:
    """
    return {"item_id": item_id}


@app.get("/cost/{individual_cost:float}")
async def read_individual_cost(individual_cost):
    """
    Read the individual cost
    :param individual_cost:
    :return:
    """
    return {"individual_cost": individual_cost}


@app.get("/users/me")
async def read_user_me():
    """
    Read Username
    :return:
    """
    return {"user_name": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """
    Read UserId
    :param user_id:
    :return:
    """
    return {"user_id": user_id}


class Item(BaseModel):
    """
    Item Subclass of Base Model to encapsulate Tax Data
    """
    name: str
    description: Optional[str] = None
    price: float
    # tax = Optional[float] = None


@app.post("/items/")
async def create_item(item: Item):
    """
    Create the item
    :return:
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item


@app.put("/items/{item_id}")
async def push_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


fake_items_db= [
    {"item_name":"Foo"},
    {"item_name": "Bar"},
    {"item_name":"Baz"}
]
@app.get("/items/")
async def read_item(skip:int=0, limit:int=10):
    """

    :param skip:
    :param limit:
    :return:
    """
    return fake_items_db[skip:skip+limit]


# @app.get("/items/{item_id}")