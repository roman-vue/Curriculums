from flask import Flask
from flask_pymongo import PyMongo
from routes.person import person

app = Flask(__name__)
#Registro de Blueprints
app.register_blueprint(person)

#Conexion Base de datos
app.config['MONGO_URI'] = 'mongodb+srv://Curr_ADMIN:Kv4eGREjttoWv7qL@curriculumsdb.rd9hs.mongodb.net/Curriculums_ex?retryWrites=true&w=majority'
mongo = PyMongo(app)