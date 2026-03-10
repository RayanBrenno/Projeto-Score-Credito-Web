from bson import ObjectId


def serialize_mongo_doc(doc: dict) -> dict:
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


def is_valid_object_id(value: str) -> bool:
    return ObjectId.is_valid(value)