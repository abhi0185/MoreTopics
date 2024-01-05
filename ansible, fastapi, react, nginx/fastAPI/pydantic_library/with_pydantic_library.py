from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
async def create_item_with_pydantic(item: Item):
    # Pydantic has already validated the data in `item`
    # Use the validated data directly
    return item


# Here no need to add validation check to see name, price, is_offer is present or not in post request
# pydantic library provide validation support. Here we need to import and use BaseModel of pydantic library

# here you manually add to check or validate like name or price is present in coming post request or not

# using swagger we can paas {"name": "abhi", "price": 121, "is_offer": false}. Return 200
#                   if paas {"name": "abhi", "is_offer": false}. It raise Exception
