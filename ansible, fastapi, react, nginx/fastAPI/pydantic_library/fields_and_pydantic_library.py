from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item1(BaseModel):
    name: str
    price: float
    is_offer: bool = None

class Item2(BaseModel):
    name: str       # mandatory field
    description: str = Field("give info", title="Description here", max_length=50)  # deault value set and max length define"
    price: float = Field(..., gt=0, description="value should float greater than 0")    # no default value but value should > 0
    is_offer: bool = None   # field is optional

@app.post("/items/")
async def create_item_with_pydantic(item: Item1):
    # Pydantic has already validated the data in `item`
    # Use the validated data directly
    return item

@app.post("/field_items/")
async def create_item_with_pydantic(item: Item2):
    # Pydantic has already validated the data in `item`
    # Use the validated data directly
    return item


# Here no need to add validation check to see name, price, is_offer is present or not in post request
# pydantic library provide validation support. Here we need to import and use BaseModel of pydantic library

# here you manually add to check or validate like name or price is present in coming post request or not

# using swagger we can paas {"name": "abhi", "price": 121, "is_offer": false}. Return 200
#                   if paas {"name": "abhi", "is_offer": false}. It raise Exception
