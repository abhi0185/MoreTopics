from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/items/")
async def create_item_without_pydantic(item_data: dict):
    if "name" not in item_data or "price" not in item_data:
        raise HTTPException(status_code=400, detail="Incomplete item data")

    name = item_data["name"]
    price = item_data["price"]
    
    # Additional validation logic can be added here
    # Process the data, maybe save it to a database, etc.

    return {"name": name, "price": price}


# here you manually add to check or validate like name or price is present in coming post request or not

# using swagger we can paas {"name": "abhi", "price": "55"}. Return 200
#                   if paas {"name": "abhi"}. It raise Exception

