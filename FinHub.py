from pymongo import MongoClient

connection_string = "mongodb+srv://raa9917:Rr12112002@cluster0.p902n.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client["test_db"]
collection = db["test_collection"]
sample_data = {"name": "John Doe", "age": 30, "city": "New York"}
collection.insert_one(sample_data)

print("Document inserted successfully!")
