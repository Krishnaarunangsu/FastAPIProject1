from fastapi import FastAPI

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
