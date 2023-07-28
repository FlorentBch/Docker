# Import de flask
from flask import Flask, jsonify, request
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# Docker compose up --build pour rebuild une image

# Création de mon application Flask
app = Flask(__name__)

host= os.environ.get("MONGO_HOST", "localhost")
port = 27017

client = MongoClient(host=host, port=port)
mabdd = client.demo

col = mabdd.users

# Premiere route sur "/"
@app.route("/")
def hello_world():
    informations = "hello_world\n"+str(mabdd)
    return(informations)

# Test flask 123
@app.route("/poulet/<msg>",methods=["GET"])
def poulet(msg):
    return f'Bonjour {msg}'

# Méthode qui renvoie tous les users
@app.route("/users", methods=['GET'])
def get_users():
    datas = list(col.find())
    for data in datas:
        data["_id"] = str(data["_id"])
    return jsonify({"users": datas})

# Méthode qui renvoie un id
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    data = col.find_one({'_id': ObjectId(id)})
    data['_id'] = str(data['_id'])
    return jsonify({"user":data})

#  Methode pour créer un user
@app.route("/users",methods=["POST"])
def create_user():
    data = request.get_json()
    result = col.insert_one(data)
    data['_id'] = str(result.inserted_id)
    return jsonify({"new_user": data})

# Méthode pour mettre à jour
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    data['_id'] = ObjectId(id)
    result = col.replace_one({'_id':ObjectId(id)}, data)
    data["_id"] = str(result.upserted_id)
    return jsonify({"update_user :": data})

# Méthode pour delete
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    data_deleted = col.find_one({"_id": ObjectId(id)})
    col.delete_one({"_id": ObjectId(id)})
    return jsonify({"Deleted_user :": data_deleted})

# Lancement de mon application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001,debug=True)