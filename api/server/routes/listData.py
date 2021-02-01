from ..models.userData import itemDataSchema
from fastapi import APIRouter, Request, Body
from fastapi.encoders import jsonable_encoder


from ..database import (
    addItem,
    deleteItem,
    getItemData,
) 


from ..models.userData import (
    ResponseModel,
    itemDataSchema,
    ErrorResponseModel,
)

router = APIRouter()

@router.get("/", response_description="Getting item data")
async def getItem(request:Request, userName:str, itemName:str):
    if (userName != "" and itemName !=""):
        itemCollection = request.app.mongodb[userName]
        item = await getItemData(itemCollection, itemName)
        if item:
            return ResponseModel(item, "Item data retrieved successfully")
        return ErrorResponseModel("An error occurered", 404, "Item does not exist")
    return ErrorResponseModel("An error occured", 404, "Invalid input value")


@router.post("/", response_description="Adding item data")
async def insertItem(request:Request, userName:str, item:itemDataSchema):
    if (userName != "" and item.name !=""):
        userCollection = request.app.mongodb.userData
        itemCollection = request.app.mongodb[userName]
        item = await addItem(userCollection, itemCollection, userName, item)
        if item:
            return ResponseModel(item, "Item added successfully")
        return ErrorResponseModel("An error occurered", 404, "List or User does not exist")
    return ErrorResponseModel("An error occured", 404, "Invalid input value")

@router.delete("/", response_description="delete item from db")
async def removeItem(request:Request, userName:str, itemName:str):
    if (userName != "" and itemName !=""):
        userCollection = request.app.mongodb.userData
        itemCollection = request.app.mongodb[userName]
        item = await deleteItem(userCollection, itemCollection, userName, itemName)
        if item:
            return ResponseModel(itemName, "Item removed successfully")
        return ErrorResponseModel("An error occurered", 404, "Item does not exist")
    return ErrorResponseModel("An error occured", 404, "Invalid input value")