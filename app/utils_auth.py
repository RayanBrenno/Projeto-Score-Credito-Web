from app.database import db

users_collection = db["users"]

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

def get_user_by_id(user_id):
    from bson import ObjectId
    return users_collection.find_one({"_id": ObjectId(user_id)})

def create_user(data: dict):
    result = users_collection.insert_one(data)
    return users_collection.find_one({"_id": result.inserted_id})