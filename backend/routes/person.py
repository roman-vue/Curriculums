from flask import Blueprint, request
from Class.Person import Person


person = Blueprint('person', __name__)
PersonC = Person()

@person.route("/createPerson", methods = ['POST'])
def createPerson():

    name = request.json["name"]
    lastname = request.json["lastname"]
    profession = request.json["profession"]
    phone = request.json["phone"]

    data = {'name': name, 'lastname': lastname, 'profession': profession, 'phone': phone}

    resp = PersonC.createPerson(data)
    return resp
 
