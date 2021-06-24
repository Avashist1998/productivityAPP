import os
from fastapi import FastAPI
from .routes.userData import router as userRouter
from .routes.listData import router as listRouter
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
app.include_router(userRouter, tags=["User"], prefix="/user")
app.include_router(listRouter, tags=["List"], prefix="/list")

    # "http://localhost",
    # "http://192.168.1.201",
    # "http://192.168.1.129",
    # "http://localhost:8000",
    # "http://localhost:8080",
    # "http://192.168.1.201:3000"
    # "http://192.168.1.255:3000"
    # "http://192.168.1.201:6070",
    # "http://192.168.1.255:6070"
origins = [
    "http://192.168.1.201:6070",
    "http://192.168.1.201:6050",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
	app.mongodb_client = AsyncIOMotorClient(os.getenv("DB_URL"))
	app.mongodb = app.mongodb_client[os.getenv("DB_NAME")]
	
@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()



@app.get("/", tags=["Root"])
async def read_root():
    return {"message":"app main page"}

