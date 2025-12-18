from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
mongo_uri = os.environ.get("MONGO_URI", "mongodb://database:27017/")
client = MongoClient(mongo_uri)
db = client["mydb"]
collection = db["messages"]

@app.route("/api/message")
def message():
    doc = collection.find_one() or {"message": "Hello from MongoDB!"}
    return jsonify(doc)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
