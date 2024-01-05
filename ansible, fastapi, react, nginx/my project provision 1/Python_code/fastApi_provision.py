from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for now (Replace * with your frontend's URL in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/regions')
async def get_regions():
    regns = [
    {
        "code": "af-south-1",
        "name": "Africa: Cape Town",
        "description": "Africa (Cape Town) Region",
        "is_active": 0,
        "create_date": "2023-10-12 04:58:13"
    },
    {
        "code": "ap-south-1",
        "name": "Asia Pacific: Mumbai",
        "description": "Asia Pacific (Mumbai) Region",
        "is_active": 0,
        "create_date": "2023-10-12 04:58:13"
    }]
    return {'Regions': regns}

@app.get('/environments')
async def get_environments():
    envsn = [
    {
        "id": "0x000D9F085D7C440B897D0695E218A6E3",
        "name": "aut entr dev0002 170",
        "status": "decommissioned",
        "region_code": "US: Virginia",
        "kony_account_id": 100000059,
        "create_date": "2023-11-20 05:01:14",
        "is_env_disabled": 0,
    },
    {
        "id": "0x001A4D233735451CA445CAE5934B4E3F",
        "name": "BVT-AUTHPAID-0e5d79",
        "status": "decommissioned",
        "region_code": "US: Virginia",
        "kony_account_id": 100000068,
        "create_date": "2023-11-20 05:01:14",
        "is_env_disabled": 0,
    }]
    return {'Environments': envsn}

