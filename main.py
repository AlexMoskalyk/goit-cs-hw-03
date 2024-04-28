import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client["goit-cs-hw-03"]

parser = argparse.ArgumentParser(description="Add a new cat")
parser.add_argument("--action", help="[create, read, update, delete]")
parser.add_argument("--id", help="ID of the cat")
parser.add_argument("--name", help="Name of the cat")
parser.add_argument("--age", help="Age of the cat")
parser.add_argument("--features", help="Features of the cat", nargs="+")

args = vars(parser.parse_args())
action = args["action"]
pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]


def read():
    cats = db.cats.find()
    return cats


def create(name, age, features):
    return db.cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })

def read_by_name(name):
    cat = db.cats.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Cat not found")


def update_age_by_name(name, age):
    result = db.cats.update_one({"name": name}, {"$set": {"age": age}})
    if result.modified_count:
        print("Age updated successfully")
    else:
        print("No updates made")       


def add_feature_by_name(name, feature):
    result = db.cats.update_one({"name": name}, {"$push": {"features": feature}})
    if result.modified_count:
        print("Feature added successfully")
    else:
        print("No features added")

def delete_by_name(name):
    result = db.cats.delete_one({"name": name})
    if result.deleted_count:
        print("Cat deleted successfully")
    else:
        print("No cat found to delete")

def update(pk, name, age, features):
    return db.cats.update_one({"_id": ObjectId(pk)}, {"$set": {"name": name, "age": age, "features": features}})


def delete_all():
    result = db.cats.delete_many({})
    print(f"Deleted {result.deleted_count} cats")

def delete(pk):
    return db.cats.delete_one({"_id": ObjectId(pk)})


if __name__ == "__main__":
    match action:
        case "create":
            r = create(name, age, features)
            print(r.inserted_id)
        case "read":
            [print(cat) for cat in read()]
        
        case "read_by_name":
            read_by_name(name)

        case "update":
            r = update(pk, name, age, features)
            print(r.modified_count)
        
        case "update_age_by_name":
            update_age_by_name(name, age)
            
        case "add_feature_by_name":
            add_feature_by_name(name, "new_feature")

        case "delete":
            r = delete(pk)
            print(r.deleted_count)
        
        case "delete_by_name":
            delete_by_name(name)
            
        case "delete_all":
            delete_all()
        case _:
            print("Wrong action")