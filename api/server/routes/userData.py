from fastapi import APIRouter, Request, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    addUser,
    # deleteUser,
    retrieveUserData,
)   

from ..models.userData import (
    ResponseModel,
    userDataSchema,
    ErrorResponseModel,
)

router = APIRouter()

@router.get("/", response_description="Getting user items")
async def getUserData(request:Request, userName:str):
    collection = request.app.mongodb.userData
    user = await retrieveUserData(collection, userName)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurered", 404, "User does not exist")

@router.post("/", response_description="Adding user")
async def addUserData(request:Request, userName:str):
    collection = request.app.mongodb.userData
    user = await addUser(collection, userName)
    if user:
        return user
    return ErrorResponseModel("An error occurered", 404, "User does not exist")