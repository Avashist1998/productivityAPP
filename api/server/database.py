from bson.objectid import ObjectId
from datetime import date, time


async def retrieveUserData(userCollection, userName):
    user = await userCollection.find_one({"user":{"$eq":userName}})
    if user:
        return user_helper(user)
    return user 

async def addUser(userCollection, userName):
    newUser = {
        "user":userName,
        "itemNames":[],
    }
    result = await userCollection.insert_one(newUser)
    if result.acknowledged:
        return await retrieveUserData(userCollection, userName)
    return result.acknowledged

async def getItemData(itemCollection, itemName):
    item = await itemCollection.find_one({"name":{"$eq":itemName}})
    if item:
        return item_helper(item)
    return item

async def addItem(userCollection, itemCollection, userName, data):
    newItem = data.dict()
    user = await userCollection.find_one({
        "user":{"$eq":userName}
    })
    if user:
        user = user_helper(user)
        user["itemNames"].append(newItem['name'])
        result = await userCollection.update_one(
            {'_id':ObjectId(user['id'])},
            {"$set":{"itemNames":user["itemNames"]}}
        )
        if result.acknowledged:
            # newItem['d'] = int(newItem['d'].strftime('%Y%m%d'))
            result = await itemCollection.insert_one(newItem)
            if result.acknowledged:
                return await getItemData(itemCollection, newItem['name'])
        return result.acknowledged
    return user

async def deleteItem(userCollection, itemCollection, userName, itemName):
    user = await userCollection.find_one({
        "user":{"$eq":userName}
    })
    if user:
        user = user_helper(user)
        user["itemNames"].remove(itemName)
        result = await userCollection.update_one(
            {'_id':ObjectId(user['id'])},
            {"$set":{"itemNames":user["itemNames"]}}
        )
        if result.acknowledged:
            result = await itemCollection.delete_one(
                {"name":{"$eq":itemName}}
            )
    return user 


def user_helper(user)->dict:
    return {
        'id':str(user['_id']),
        'user':str(user['user']),
        'itemNames':list(user["itemNames"])
    }


def item_helper(item)->dict:
    return {
        'id':str(item['_id']),
        'name':str(item['name']),
        'd':str(item['d'])
    }