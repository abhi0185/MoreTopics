from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/add')
async def add_numbers(a: int, b: int):
    return {"result": a + b}

#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1',port='8001')
