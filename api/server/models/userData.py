from typing import List
from datetime import date, time
from pydantic import BaseModel, Field

class userDataSchema(BaseModel):
    name:str = Field(...)
    itemList:List[str] = Field(...)
    class Config:
        schema_extra = {
            "example":{
                "name": "Joe-Doe",
                "itemList":[
                    "study",
                    "workout"
                ]
            }
        }

class itemDataSchema(BaseModel):
    name:str = Field(...)
    d: str = None
    # t: time = None 
    class Config:
        schema_extra = {
            "example":{
                "name":"Sleep",
                "d":"2021-06-28"
            }
        }

def ResponseModel(data,message):
    return {
        "data": [data],
        "code": 200,
        "message":message
        }

def ErrorResponseModel(error, code, message):
    return {
        "error": error, 
        "code": code, 
        "message": message
        }