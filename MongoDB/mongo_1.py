import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# ** create database **

mydb = myclient["mydatabase"]
# print(mydb)

# print(myclient.list_database_names())
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#     print("The database exists...")

# ** create collection **

customer_col = mydb["customers"]
seller_col = mydb["sellers"]
# print(customer_col)
# print(seller_col)

# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")

# ** Insert into collection **

customer1 = {
    "name": "kabbya",
    "address": "mohakhali"
}

x = customer_col.insert_one(customer1)

print(x)
print(x.inserted_id)
