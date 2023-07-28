"""
Exemple de communication avec une base mongoDB
Lexique:
    Base de donnée <=> database
    Table <=> collection
    row(ligne) <=> document
"""
from pymongo import MongoClient
# Info de ma base de données
host = 'localhost'
port = 27017

# Création du Mongo client
client = MongoClient(host=host, port=port)

#  Récupération de ma base de données
mabdd = client.demo

print("mabdd : \n", mabdd)

# Récupération d'une collection
col = mabdd.users

print('ma collection_type : \n', type(col))
print("ma collection : \n", col)

# Ajout des data dans ma bdd => format JSON
new_data = {
    'nom':"Bidouille",
    'prenom':"Bob",
    'age':42
}

# Insertion de mon document JSON
response_new_id = col.insert_one(new_data)
# Récupération de l'id à partir de l'objectID
new_id = str(response_new_id.inserted_id)
# Attribution de son id à ma nouvel data enregistrée
new_data["_id"] = new_id
print(new_data)

# Récupération de tous les users de ma colletion
mes_users = col.find()
print(list(mes_users))