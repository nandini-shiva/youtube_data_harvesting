from pymongo import MongoClient

# Create a MongoClient object
client = MongoClient('mongodb://localhost:27017/')

# Access a database
db = client['mydatabase']

# Access a collection
collection = db['mycollection']

# Insert a document
document = {"name": "John", "age": 30}
# collection.insert_one(document)

# Update a document
query = {"name": "John"}
new_values = {"$set": {"age": 32}}
collection.update_one(query, new_values)

# Delete documents
query = {"age": {"$lt": 30}}
collection.delete_many(query)


# Query documents
results = collection.find({"age": {"$gt": 25}})
for result in results:
    print(result)

# Close the MongoDB connection
client.close()

# print(collection)