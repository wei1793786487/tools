import pymongo

myclient = pymongo.MongoClient("mongodb://49.232.54.164:7758/")
mydb = myclient["question"]
mycol = mydb["list"]

def insertOne(data):
    try:
        x = mycol.insert_one(data)
        print(x.inserted_id)
    except:
        pass
